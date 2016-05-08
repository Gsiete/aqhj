from django.shortcuts import render
import aqhorajuega.functions
from main.models import Match
from django.utils import timezone


def index(request):
    next_match = Match.objects.filter(time__gte=timezone.now()).order_by('time')[0]
    user_city = aqhorajuega.functions.get_user_city(request)
    user_city = user_city if user_city else next_match.stadium.city
    time_format = request.GET.get('format', '24')
    following_matches = [next_match for _ in range(5)]

    return render(request, 'main/index.html', {
       'following_matches': following_matches,
       'time_format': time_format,
       'next_match': next_match,
       'user_city': user_city})
