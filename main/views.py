from django.shortcuts import render
import aqhorajuega.functions
from main.models import Match
from django.utils import timezone


def index(request):
    next_match = Match.objects.filter(time__gte=timezone.now()).order_by('time')[0]
    tz = aqhorajuega.functions.get_user_timezone(request)

    return render(request, 'main/index.html', {'next_match': next_match, 'timezone': tz})
