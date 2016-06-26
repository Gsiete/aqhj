from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Q, Max, Count
from django.http import HttpResponse, Http404
from django.utils import timezone

from main.functions import aqhj_render
from main.models import Match, Season, TeamSeasonGroup, Summary, ThreeArticles, Article
from django.shortcuts import get_object_or_404, redirect


def index(request):
    from django.utils import translation
    user_language = 'es_AR'
    translation.activate(user_language)
    match_filter = add_check_credentials(Q(end_time__gte=timezone.now()), request)
    next_match = Match.objects.filter(match_filter).order_by('time')[0]
    articles_filter = add_check_credentials(Q(priority_in_home__isnull=False), request, False)
    articles = Article.objects.filter(articles_filter).order_by('-priority_in_home', '-created_at').select_subclasses()[:7]

    fm_filter = match_filter & ~Q(id=next_match.id)
    following_matches = Match.objects.filter(fm_filter).order_by('time')[:6]

    return aqhj_render(request, 'main/home.html',
                       {'following_matches': following_matches, 'match': next_match, 'home': True,
                        'articles': articles})


def match_before(request, **kwargs):
    match_filter = add_check_credentials(Q(**kwargs), request)
    try:
        match = Match.objects.get(match_filter)
    except Match.DoesNotExist:
        if kwargs['game_in_season'] and kwargs['game_in_season'][:5] == 'fecha':
            try:
                kwargs['game_in_season'] = kwargs['game_in_season'].replace('fecha', 'fase-de-grupo-partido')
                match = Match.objects.get(add_check_credentials(Q(**kwargs), request))
                return redirect(match.url, permanent=True)
            except Match.DoesNotExist:
                raise Http404('No %s matches the given query.' % Match._meta.object_name)

        raise Http404('No %s matches the given query.' % Match._meta.object_name)

    three_articles = ThreeArticles.objects.filter(add_check_credentials(Q(match=match), request, False)).first()

    following_matches = None
    if timezone.now() < match.end_time:
        fm_filter = ~Q(id=match.id) & Q(end_time__gte=timezone.now())
        fm_filter = add_check_credentials(fm_filter, request)
        following_matches = Match.objects.filter(fm_filter).order_by('time')[:6]

    return aqhj_render(request, 'main/match-before.html',
                       {'following_matches': following_matches, 'match': match, 'three_articles': three_articles})


def past_match(request, **kwargs):
    match_filter = add_check_credentials(Q(**kwargs), request)
    try:
        match = Match.objects.get(match_filter)
    except Match.DoesNotExist:
        raise Http404('No %s matches the given query.' % Match._meta.object_name)
    summary = Summary.objects.filter(add_check_credentials(Q(match=match), request, False)).first()

    return aqhj_render(request, 'main/match-after.html',
                       {'match': match, 'summary': summary})


def last_matches(request):
    match_filter = add_check_credentials(Q(end_time__lte=timezone.now()), request)
    latest_matches = Match.objects.filter(match_filter).order_by('-time')[:10]

    return aqhj_render(request, 'main/last-matches.html', {'last_matches': latest_matches})


def redirect_aqhj(request, url):
    return redirect('http://%s/%s' % (get_current_site(request).domain, url), permanent=True)


def group_round_positions(request, **kwargs):
    # ToDo: try to see if the issue with group by was the name
    season = get_object_or_404(Season, **kwargs)
    teamstats = TeamSeasonGroup.objects.filter(season=season)

    return aqhj_render(request, 'main/position-table.html', {'season': season, 'teamstats': teamstats})


def final_phase_positions(request, **kwargs):
    season = get_object_or_404(Season, **kwargs)
    match_filter = add_check_credentials(Q(game_in_phase__isnull=False, season=season), request, True, False)
    matches = Match.objects.filter(match_filter).order_by('game_in_season', 'game_in_phase').all()
    phases_order = {'ronda-de-16': 1, 'cuartos-de-final': 2, 'semi-final': 3, 'final': 4}
    phases_short = {'ronda-de-16': 'Octavos', 'cuartos-de-final': 'Cuartos', 'semi-final': 'Semi', 'final': 'Final'}
    phases_long = {'ronda-de-16': 'Ronda de 16', 'cuartos-de-final': 'Cuartos de final', 'semi-final': 'Semifinal',
                   'final': 'Final'}

    matches_ordered = {'ronda-de-16': [], 'cuartos-de-final': [], 'semi-final': [], 'final': []}
    for match in matches:
        if match.game_in_season in matches_ordered.keys():
            matches_ordered[match.game_in_season].append(match)
    # Remove empty phases
    matches_ordered = dict((k, v) for k, v in matches_ordered.items() if v)
    # print(matches_ordered)
    matches_ordered = [matches_ordered[k] for k in sorted(matches_ordered, key=phases_order.__getitem__)]
    third_place_match_filter = add_check_credentials(Q(game_in_season='partido-tercer-puesto', season=season), request,
                                                     True, False)
    third_place_match = Match.objects.filter(third_place_match_filter).first()

    return aqhj_render(request, 'main/bracket.html',
                       {'matches': matches_ordered, 'phases': phases_long, 'phases_short': phases_short,
                        'third_place_match': third_place_match, 'season': season})


def add_check_credentials(q_filter, request, for_match=True, domain_filter=True):
    if not request.user.is_authenticated():
        q_filter &= Q(is_published=True)
    if domain_filter:
        if for_match:
            q_filter &= Q(team_a__site=get_current_site(request)) | Q(team_b__site=get_current_site(request))
        else:
            q_filter &= Q(site=get_current_site(request))

    return q_filter
