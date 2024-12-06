# ML_Models/templatetags/custom_filters.py
from django import template

register = template.Library()


@register.filter
def zip_lists(value, arg):
    """Zips two lists together."""
    return zip(value, arg)
