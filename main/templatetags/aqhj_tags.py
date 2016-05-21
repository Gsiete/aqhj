from django import template
from django.core.urlresolvers import get_resolver, reverse

register = template.Library()


@register.filter
def astimezone(time, tz):
    return time.astimezone(tz)


@register.filter
def astz(time, tz):
    return time.astimezone(tz).ctime()


@register.filter
def isotime(time):
    return time.isoformat()


@register.filter
def url_from_object(route, obj):
    resolver = get_resolver(None)
    parameters = resolver.reverse_dict[route][0][0][1]
    kwargs = {}
    args = []
    for field in parameters:
        field_path = field.split('__')
        kwargs[field] = str(get_value_from_field_path(obj, field_path))
        args.append(str(get_value_from_field_path(obj, field_path)))
    # return reverse(route, kwargs=kwargs)
    return reverse(route, args=args)


def get_value_from_field_path(obj, fields_path):
    value = obj
    for field in fields_path:
        value = getattr(value, field)

    return value
