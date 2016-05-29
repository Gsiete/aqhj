from django.db.models import Q
from django.http import HttpResponse, Http404
from django.utils import timezone

from main.functions import aqhj_render
from main.models import Match, Season, TeamSeasonGroup
from django.shortcuts import get_object_or_404, redirect


def index(request):
    from django.utils import translation
    user_language = 'es_AR'
    translation.activate(user_language)
    match_filter = add_check_credentials(Q(end_time__gte=timezone.now()), request)
    next_match = Match.objects.filter(match_filter).order_by('time')[0]

    fm_filter = match_filter & ~Q(id=next_match.id)
    following_matches = Match.objects.filter(fm_filter).order_by('time')[:6]

    return aqhj_render(request, 'main/match-before.html',
                       {'following_matches': following_matches, 'match': next_match, 'home': True})


def match_before(request, today=False, **kwargs):
    match_filter = add_check_credentials(Q(**kwargs), request)
    try:
        match = Match.objects.get(match_filter)
    except Match.DoesNotExist:
        raise Http404('No %s matches the given query.' % Match._meta.object_name)

    if timezone.now() > match.end_time or today and not match.is_today:
        return redirect(match.url, permanent=True)

    fm_filter = ~Q(id=match.id) & Q(end_time__gte=timezone.now())
    fm_filter = add_check_credentials(fm_filter, request)
    following_matches = Match.objects.filter(fm_filter).order_by('time')[:6]

    return aqhj_render(request, 'main/match-before.html', {'following_matches': following_matches, 'match': match})


def past_match(request, **kwargs):
    match_filter = add_check_credentials(Q(**kwargs), request)
    try:
        match = Match.objects.get(match_filter)
    except Match.DoesNotExist:
        raise Http404('No %s matches the given query.' % Match._meta.object_name)

    return aqhj_render(request, 'main/match-after.html', {'match': match})


def last_matches(request):
    match_filter = add_check_credentials(Q(end_time__lte=timezone.now()), request)
    latest_matches = Match.objects.filter(match_filter).order_by('-time')[:10]

    return aqhj_render(request, 'main/last-matches.html', {'last_matches': latest_matches})


def group_round_positions(request, **kwargs):
    # ToDo: try to see if the issue with group by was the name
    season = get_object_or_404(Season, **kwargs)
    teamstats = TeamSeasonGroup.objects.filter(season=season)

    return aqhj_render(request, 'main/position-table.html', {'season': season, 'teamstats': teamstats})


def add_check_credentials(q_filter, request):
    if not request.user.is_authenticated():
        q_filter &= Q(is_published=True)
    return q_filter
