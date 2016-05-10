from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError
import random
from cities.models import City, Country
ips = {'ar': '201.231.108.8'}


def get_user_city(request):
    g = GeoIP2()
    ip = get_client_ip(request)
    if ip == "127.0.0.1":
        get_random_ip(g)

    fake_ip = request.GET.get('fake-ip', False)
    if fake_ip:
        if ips.get(fake_ip, False):
            ip = ips.get(request.GET.get('fake-ip', False), False)
        elif fake_ip == 'rand':
            ip = get_random_ip(g)

    city = None
    city_internal = g.city(ip)
    if city_internal['city']:
        city_array = City.objects.filter(name=city_internal['city'], country__code2=city_internal['country_code'])[:1]
        city = city_array[0] if city_array else None

    if city is None and city_internal['country_code']:
        country = Country.objects.get(code2=city_internal['country_code'])
        city = country.capital

    return city


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_random_ip(g):
    ip = ''
    while True:
        try:
            ip = '{0}.{1}.{2}.{3}'.format(*(random.randrange(255) for _ in range(4)))
            # ip = '28.19.213.230'
            g.lat_lon(ip)
            break
        except AddressNotFoundError:
            pass
    return ip

# def get_timezone_from_coords(latitude, longitude):
#     api_response = requests.get(settings.GOOGLE_TZ_API_ENDPOINT,
#                                 {'location': '{0},{1}'.format(latitude, longitude),
#                                  'timestamp': time.time(),
#                                  'key': settings.GOOGLE_API_KEY})
#
#     api_response_dict = api_response.json()
#     if api_response_dict['status'] == 'OK':
#         return pytz.timezone(api_response_dict['timeZoneId'])
#
#     return None
