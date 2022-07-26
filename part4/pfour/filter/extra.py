from django import template

filter=template.Library()
@register.filter(name='one')
class one(value,arg):
    return value.replace(arg,' ')
