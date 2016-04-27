from django.shortcuts import render
import aqhorajuega.functions
from main.models import Match
from django.utils import timezone


def index(request):
    next_match = Match.objects.filter(time__gte=timezone.now()).order_by('time')[0]
    user_city = aqhorajuega.functions.get_user_city(request)

    return render(request, 'main/index.html', {'next_match': next_match, 'user_city': user_city})
