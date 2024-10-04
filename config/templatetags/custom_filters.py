from django import template

register = template.Library()

@register.filter(name='length_is')
def length_is(value, arg):
    """Returns True if the length of the value is equal to the argument."""
    try:
        return len(value) == int(arg)
    except (ValueError, TypeError):
        return False
