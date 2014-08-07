from django import template

from session_security.settings import WARN_AFTER, EXPIRE_AFTER, UNSAVED_FORM_WARNING

register = template.Library()


@register.filter
def expire_after(request):
    return EXPIRE_AFTER


@register.filter
def warn_after(request):
    return WARN_AFTER


@register.filter
def unsaved_form_warning(request):
    return UNSAVED_FORM_WARNING