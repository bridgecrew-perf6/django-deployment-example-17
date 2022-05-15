from django import template

register = template.Library()
@register.filter(value='cut')
def cut(value,arg):
    """
    This cut out all value of "arg" from the string!

    """
    return value.replace(arg,'')

#register.filter('cut',cut)
