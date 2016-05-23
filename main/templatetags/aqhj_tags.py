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


@register.filter
def timediff(match, user_city):
    td = match.stadium_time.utcoffset() - match.time.astimezone(user_city.timezone).utcoffset()
    hours = td.days * 24 + td.seconds // 3600
    return hours if hours <= 0 else '+' + str(hours)