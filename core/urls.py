from django.conf.urls import patterns, url

urlpatterns = patterns('core.views',
    url(r'^(?P<page>\w+)/$', 'page', name='page'),
)