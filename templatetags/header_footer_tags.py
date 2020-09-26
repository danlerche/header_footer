from django import template
from header_footer.models import Logo, Alert, FooterColumn, FooterColumnTwo

register = template.Library()

# Logo snippet
@register.inclusion_tag('header_footer/logo.html', takes_context=True)
def logo(context):
    return {
        'logo': Logo.objects.all(),
        'request': context['request'],
    }

# Alert snippet
@register.inclusion_tag('header_footer/alerts.html', takes_context=True)
def green_alerts(context):
    return {
        'green_alerts': Alert.objects.filter(alert_colour='G', enable_alert=True).order_by('-alert_date'),
        'request': context['request'],
    }
@register.inclusion_tag('header_footer/alerts.html', takes_context=True)
def red_alerts(context):
    return {
        'red_alerts': Alert.objects.filter(alert_colour='R', enable_alert=True).order_by('-alert_date'),
        'request': context['request'],
    }
@register.inclusion_tag('header_footer/alerts.html', takes_context=True)
def all_alerts(context):
    return {
        'all_alerts': Alert.objects.all(),
        'request': context['request'],
    }
# Footer Column snippet
@register.inclusion_tag('header_footer/footer_columns.html', takes_context=True)
def footer_column(context):
    return {
        'footer_column': FooterColumn.objects.all(),
        'request': context['request'],
    }

# Footer Column two snippet
@register.inclusion_tag('header_footer/footer_columns.html', takes_context=True)
def footer_column_two(context):
    return {
        'footer_column_two': FooterColumnTwo.objects.all(),
        'request': context['request'],
    }
