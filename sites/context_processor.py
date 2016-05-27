from django.core.urlresolvers import resolve
from django.db.models import Q

from sites.models import RouteConfig


# ToDo: remove route_cp when this is ready
def route_config_cp(request):
    filter_q = add_check_credentials(request, route=resolve(request.path_info).url_name)
    route_configs = RouteConfig.objects.filter(filter_q)
    return {
        'route_config': route_configs[0] if route_configs else None
    }


def add_check_credentials(request, **kwargs):
    return Q(kwargs) if request.user.is_authenticated() else Q(kwargs) & Q(is_published=True)
