from aqhorajuega.functions import aqhj_render
from main.models import Match
from django.utils import timezone


def index(request):
    next_match = Match.objects.filter(time__gte=timezone.now()).order_by('time')[0]
    following_matches = [next_match for _ in range(5)]

    return aqhj_render(request, 'main/index.html', {'following_matches': following_matches, 'next_match': next_match})


def ucf(str):
    str_a=str.split('_')
    n_str = '_'.join([s[0].upper() + s[1:] for s in str_a])
    return n_str.replace('.','')
