from datetime import timedelta

from django.db.models import Q
from django.utils import timezone

from main.functions import aqhj_render
from main.models import Match
from django.shortcuts import get_object_or_404


def index(request):
    next_match = Match.objects.filter(time__gte=timezone.now()).order_by('time')[0]
    following_matches = Match.objects.filter(time__gte=timezone.now()).order_by('time')[1:7]

    return aqhj_render(request, 'main/match-before.html',
                       {'following_matches': following_matches, 'next_match': next_match, 'home': True})


def match_before(request, **kwargs):
    today = kwargs.pop('hoy', False)
    time_criteria = {'time__gte': timezone.now()}
    if today:
        time_criteria['time__lte'] = timezone.now() + timedelta(1)
    kwargs.update(time_criteria)
    next_match = get_object_or_404(Match, **kwargs)
    # following_matches = Match.objects.filter(time__gte=next_match.time).order_by('time')[1:7]
    following_matches = Match.objects.filter(~Q(id=next_match.id, time__lt=timezone.now())).order_by('time')[1:7]

    return aqhj_render(request, 'main/match-before.html',
                       {'following_matches': following_matches, 'next_match': next_match})


def past_match(request, **kwargs):
    last_match = get_object_or_404(Match, **kwargs)

    return aqhj_render(request, 'main/match-after.html', {'match': last_match})


def last_matches(request):
    latest_matches = Match.objects.filter(time__lte=timezone.now()).order_by('-time')[:10]

    return aqhj_render(request, 'main/last-matches.html', {'last_matches': latest_matches})