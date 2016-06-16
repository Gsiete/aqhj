from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Q
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
    article = Article.objects.filter(add_check_credentials(Q(), request, False)).order_by('-created_at').first()
    summary, three_articles = None, None
    if article:
        try:
            three_articles = article.threearticles
        except ThreeArticles.DoesNotExist:
            try:
                summary = article.summary
            except Summary.DoesNotExist:
                pass

    fm_filter = match_filter & ~Q(id=next_match.id)
    following_matches = Match.objects.filter(fm_filter).order_by('time')[:6]

    return aqhj_render(request, 'main/match-before.html',
                       {'following_matches': following_matches, 'match': next_match, 'home': True,
                        'three_articles': three_articles, 'summary': summary})


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

    if timezone.now() > match.end_time:
        return redirect(match.url, permanent=True)

    three_articles = ThreeArticles.objects.filter(add_check_credentials(Q(match=match), request, False)).first()
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
    three_articles = ThreeArticles.objects.filter(add_check_credentials(Q(match=match), request, False)).first()

    return aqhj_render(request, 'main/match-after.html',
                       {'match': match, 'summary': summary, 'three_articles': three_articles})


def last_matches(request):
    match_filter = add_check_credentials(Q(end_time__lte=timezone.now()), request)
    latest_matches = Match.objects.filter(match_filter).order_by('-time')[:10]

    return aqhj_render(request, 'main/last-matches.html', {'last_matches': latest_matches})


def redirect_aqhj(request, url):
    return redirect(url, permanent=True)


def group_round_positions(request, **kwargs):
    # ToDo: try to see if the issue with group by was the name
    season = get_object_or_404(Season, **kwargs)
    teamstats = TeamSeasonGroup.objects.filter(season=season)

    return aqhj_render(request, 'main/position-table.html', {'season': season, 'teamstats': teamstats})


def add_check_credentials(q_filter, request, for_match=True):
    if not request.user.is_authenticated():
        q_filter &= Q(is_published=True)
    if for_match:
        q_filter &= Q(team_a__site=get_current_site(request)) | Q(team_b__site=get_current_site(request))
    else:
        q_filter &= Q(site=get_current_site(request))

    return q_filter
