from django.utils import timezone

from main.functions import aqhj_render
from main.models import Match
from django.shortcuts import get_object_or_404


def index(request):
    next_match = Match.objects.filter(time__gte=timezone.now()).order_by('time')[0]
    following_matches = Match.objects.filter(time__gte=timezone.now()).order_by('time')[1:7]

    return aqhj_render(request, 'main/index.html', {'following_matches': following_matches, 'next_match': next_match})


def past_match(request, **kwargs):
    last_match = get_object_or_404(Match, **kwargs)

    return aqhj_render(request, 'main/past-match.html', {'match': last_match})


def last_matches(request):
    last_matches = Match.objects.filter(time__lte=timezone.now()).order_by('-time')[:10]

    return aqhj_render(request, 'main/last-matches.html', {'last_matches': last_matches})