from __future__ import absolute_import

import django
from tests.contrib.django.testapp import views

from django.conf import settings
if django.VERSION < (1, 4):
    from django.conf.urls.defaults import *  # Django 1.3
else:
    from django.conf.urls import url, patterns
from django.http import HttpResponse

def handler500(request):
    if getattr(settings, 'BREAK_THAT_500', False):
        raise ValueError('handler500')
    return HttpResponse('')

urls = (
    url(r'^render-heavy-template$', views.render_template_view, name='render-heavy-template'),
    url(r'^render-user-template$', views.render_user_view, name='render-user-template'),
    url(r'^no-error$', views.no_error, name='opbeat-no-error'),
    url(r'^no-error-slash/$', views.no_error, name='opbeat-no-error-slash'),
    url(r'^fake-login$', views.fake_login, name='opbeat-fake-login'),
    url(r'^trigger-500$', views.raise_exc, name='opbeat-raise-exc'),
    url(r'^trigger-500-ioerror$', views.raise_ioerror, name='opbeat-raise-ioerror'),
    url(r'^trigger-500-decorated$', views.decorated_raise_exc, name='opbeat-raise-exc-decor'),
    url(r'^trigger-500-django$', views.django_exc, name='opbeat-django-exc'),
    url(r'^trigger-500-template$', views.template_exc, name='opbeat-template-exc'),
    url(r'^trigger-500-log-request$', views.logging_request_exc, name='opbeat-log-request-exc'),
)


if django.VERSION >= (1, 8):
    urls += url(r'^render-jinja2-template$', views.render_jinja2_template,
        name='render-jinja2-template'),

urlpatterns = patterns('', *urls)