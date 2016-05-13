from django import template

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
