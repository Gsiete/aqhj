import time
import requests
import pytz
from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError
import random
from cities.models import City


def get_user_timezone(request):
    g = GeoIP2()
    ip = get_client_ip(request)
    if ip == "127.0.0.1":
        while True:
            try:
                ip = '{0}.{1}.{2}.{3}'.format(*(random.randrange(255) for _ in range(4)))
                # ip = '.'.join(str(random.randrange(255)) for _ in range(4))
                # ip = '28.19.213.230'
                g.lat_lon(ip)
                break
            except AddressNotFoundError:
                pass

    city_internal = g.city(ip)
    city = City.objects.filter(name=city_internal['city'], country__code2=city_internal['country_code'])[:1]
    if city:
        return city[0].timezone

    lat_lon = g.lat_lon(ip)
    return get_timezone_from_coords(*lat_lon)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_timezone_from_coords(latitude, longitude):
    api_response = requests.get(settings.GOOGLE_TZ_API_ENDPOINT,
                                {'location': '{0},{1}'.format(latitude, longitude),
                                 'timestamp': time.time(),
                                 'key': settings.GOOGLE_API_KEY})

    api_response_dict = api_response.json()
    if api_response_dict['status'] == 'OK':
        return pytz.timezone(api_response_dict['timeZoneId'])

    return None
