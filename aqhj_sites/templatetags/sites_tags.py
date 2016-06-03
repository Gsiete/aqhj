from django import template

from django.template import Template

register = template.Library()


@register.simple_tag(takes_context=True)
def parse_string_with_context(context, string_to_parse):
    return Template(string_to_parse).render(context)
