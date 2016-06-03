from django.conf import settings
from django.core.urlresolvers import resolve
from django.db.models import Q

from aqhj_sites.models import RouteConfig, DomainConfig


# ToDo: remove route_cp when this is ready
def sites_config_cp(request):
    domain_q = add_check_credentials(request, domain=request.META.get('HTTP_HOST', get_domain()))
    route_q = domain_q & Q(route=resolve(request.path_info).url_name)
    domain_configs = DomainConfig.objects.filter(domain_q)
    route_configs = RouteConfig.objects.filter(route_q)
    return {
        'route_conf': route_configs[0] if route_configs else None,
        'domain_conf': domain_configs[0] if domain_configs else None
    }


def add_check_credentials(request, **kwargs):
    return Q(**kwargs) if request.user.is_authenticated() else Q(**kwargs) & Q(is_published=True)


def get_domain():
    return settings.AQHJ_DOMAIN.replace('http://', '')