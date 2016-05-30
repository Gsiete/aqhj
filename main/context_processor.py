from django.conf import settings


def get_current_path(request):
    return {
        'current_path': request.get_full_path(),
        'domain': settings.AQHJ_DOMAIN
    }


def settings_cp(request):
    return {'BET_AFFILIATE_LINK': settings.BET_AFFILIATE_LINK}


def main_season_cp(request):
    from main.models import Season
    try:
        main_season = Season.objects.get(is_main=True)
    except Season.DoesNotExist:
        main_season = Season.objects.all()[0]
    except Season.MultipleObjectsReturned:
        main_season = Season.objects.filter(is_main=True)[0]

    return {'main_season': main_season}


def domain_team_cp(request):
    from main.models import Team
    try:
        domain_team = Team.objects.get(is_domain_team=True)
    except Team.DoesNotExist:
        domain_team = Team.objects.all()[0]
    except Team.MultipleObjectsReturned:
        domain_team = Team.objects.filter(is_domain_team=True)[0]

    return {'domain_team': domain_team}


def time_format_cp(request):
    return {'time_format': request.COOKIES.get('tformat', '24')}
