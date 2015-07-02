from django.conf.urls import patterns, url

urlpatterns = patterns('water.views',
    url(r'^feed/$', 'feed', name='feed'),
    url(r'^gallery/$', 'gallery_show', name='gallery'),
    url(r'^gallery/like_(?P<id>\d+)/$', 'likes_gallery', name='like_gallery'),
    url(r'^video/$', 'video_show', name='video'),
    url(r'^subscribe_(?P<id>\d+)/$', 'subscribe_event', name='subscribe_event'),
)