def get_current_path(request):
    return {
        'current_path': request.get_full_path(),
        'domain': 'http://aquehorajuegaargentina.com'
    }


def main_season_cp(request):
    from main.models import Season
    try:
        main_season = Season.objects.get(is_main=True)
    except Season.DoesNotExist:
        main_season = Season.objects.all()[0]
    except Season.MultipleObjectsReturned:
        main_season = Season.objects.filter(is_main=True)[0]

    return {
        'main_season': main_season
    }


def time_format_cp(request):
    return {'time_format': request.COOKIES.get('tformat', '24')}
