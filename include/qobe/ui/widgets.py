from django import template
from django.utils.html import conditional_escape


register = template.Library()


@register.filter(name='dropdown_list')
def dropdown_list(enum):
    html = format('<div class="select" tabindex="0"><span class="value">{0}</span><ul class="optList">', enum.index(0))
    for item in enum:
        html += format('<li class="option">{0}</li>', item)
    html += '</ul></div>'
    return html

