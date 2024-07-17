from datetime import datetime
from django import template

register = template.Library()

@register.filter
def format_date(value):
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")

    try:
        date_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
        return date_obj.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return value