from django.conf import settings
from django.shortcuts import render
import aqhorajuega.functions
import datetime
from main.models import Match
from cities.models import City
from django.utils import timezone


def index(request):
    next_match = Match.objects.filter(time__gte=timezone.now()).order_by('time')[0]

    city_code = request.COOKIES.get('city_code', None)
    city_is_new = not city_code
    user_city = aqhorajuega.functions.get_user_city(request) if city_is_new else City.objects.get(pk=city_code)

    user_city = user_city if user_city else next_match.stadium.city

    time_format = request.GET.get('format', '24')
    following_matches = [next_match for _ in range(5)]

    response = render(request, 'main/index.html', {
        'following_matches': following_matches,
        'time_format': time_format,
        'next_match': next_match,
        'user_city': user_city,
        'city_is_new': city_is_new
    })

    if city_is_new:
        set_cookie(response, 'city_code', user_city.id)

    return response


def set_cookie(response, key, value, days_expire=None):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                         "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN,
                        secure=settings.SESSION_COOKIE_SECURE or None)
