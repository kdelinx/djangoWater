from django.conf.urls import patterns, url

urlpatterns = patterns('core.views',
    url(r'^feed/$', 'feed', name='feed'),
    url(r'^(?P<page>\w+)/$', 'page', name='page'),
)