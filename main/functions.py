import random

from django.contrib.gis.geoip2 import GeoIP2
from django.core.urlresolvers import get_resolver, reverse
from django.shortcuts import render
from geoip2.errors import AddressNotFoundError
from django.conf import settings
import datetime

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


def aqhj_render(request, template, context):
    city_code = request.COOKIES.get('city_code', None)
    city_is_new = not city_code
    user_city = get_user_city(request) if city_is_new else City.objects.get(pk=city_code)

    time_format = request.COOKIES.get('tformat', '24')
    from main.models import Season
    try:
        main_season = Season.objects.get(is_main=True)
    except Season.DoesNotExist:
        main_season = Season.objects.all()[0]
    except Season.MultipleObjectsReturned:
        main_season = Season.objects.filter(is_main=True)[0]
    context.update({'time_format': time_format,
                    'user_city': user_city,
                    'city_is_new': city_is_new,
                    'main_season': main_season})

    response = render(request, template, context)

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


def reverse_from_object(route, obj):
    resolver = get_resolver(None)
    parameters = resolver.reverse_dict[route][0][0][1]
    kwargs = {}
    for field in parameters:
        field_path = field.split('__')
        kwargs[field] = str(get_value_from_field_path(obj, field_path))

    return reverse(route, kwargs=kwargs)


def get_value_from_field_path(obj, fields_path):
    value = obj
    for field in fields_path:
        value = getattr(value, field)

    return value
