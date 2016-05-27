from django.core.urlresolvers import resolve
from django.db.models import Q

from sites.models import RouteConfig


# ToDo: remove route_cp when this is ready
def route_config_cp(request):
    domain_q = add_check_credentials(request, domain=request.META['HTTP_HOST'])
    route_q = domain_q & Q(route=resolve(request.path_info).url_name)
    route_configs = RouteConfig.objects.filter(route_q)
    domain_configs = RouteConfig.objects.filter(route_q)
    return {
        'route_conf': route_configs[0] if route_configs else None,
        'domain_conf': route_configs[0] if domain_configs else None
    }


def add_check_credentials(request, **kwargs):
    return Q(kwargs) if request.user.is_authenticated() else Q(kwargs) & Q(is_published=True)
