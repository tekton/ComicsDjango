from django import template

register = template.Library()


@register.filter
def hexVert(value):
    """Removes all values of # from the given string and replaces with %23"""
    if value != None:
        value = value.replace("#", '%23')
        value = value.replace("!", '%21')
        value = value.replace("&", '%26')
    return value
