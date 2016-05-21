from django import template

from main.functions import reverse_from_object

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
    return reverse_from_object(route, obj)
