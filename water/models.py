# coding: utf-8
import uuid
from django.db import models
from core.models import AbstractClass
from users.models import User
from imagekit.models import ImageSpecField, ProcessedImageField
from pilkit.processors import ResizeToFill
import random, urllib, urlparse, json


def get_image_gallery(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return 'gallery/%s%s%s' % (filename[:1], filename[2:3], filename)


class News(AbstractClass):
    title = models.CharField(
        'Заголовок',
        max_length=255
    )
    body = models.TextField(
        'Новость'
    )

    class Meta:
        verbose_name = u'Новости'
        verbose_name_plural = u'новости'

    def __unicode__(self):
        return self.title


class Videos(AbstractClass):
    url = models.URLField(
        max_length=100
    )
    video_id = models.CharField(
        max_length=20,
        blank=True,
        default=''
    )
    title = models.CharField(
        'Заголовок',
        max_length=255,
        blank=True,
        default=''
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    news = models.ForeignKey(
        News,
        related_name='news_video',
        blank=True,
    )
    likes = models.ManyToManyField(
        User,
        related_name='user_likes_video',
        blank=True
    )

    class Meta:
        verbose_name = u'Видео'
        verbose_name_plural = u'видео'

    def __unicode__(self):
        return self.title

    def get_small_image_url(self):
        return 'http://img.youtube.com/vi/%s/%s.jpg' % (self.video_id, random.randint(1, 3))

    def get_hqdefault(self):
        return 'http://i1.ytimg.com/vi/%s/hqdefault.jpg' % self.video_id

    def get_mqdefault(self):
        return 'http://i1.ytimg.com/vi/%s/mqdefault.jpg' % self.video_id

    def get_sddefault(self):
        return 'http://i1.ytimg.com/vi/%s/sddefault.jpg' % self.video_id

    def get_video_id(self, url):
        link = urlparse.urlparse(url)
        if link.hostname == 'youtu.be':
            return link.path[1:]
        if link.hostname in ('www.youtube.com', 'youtube.com'):
            if link.path == '/watch':
                state = urlparse.parse_qs(link.query)
                return state['v'][0]
            if link.path[:7] == '/embed/':
                return link.path.split('/')[2]
            if link.path[:3] == '/v/':
                return link.path.split('/')[2]
        return False

    def get_meta(self, video_id):
        api_token = 'AIzaSyDW1EbrAwnT1FQanMnyB3FJIAnvXUuiKrM'
        url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id=%s&key=%s' % (video_id, api_token)
        response = json.load(urllib.urlopen(url))
        print response
        context = {
            'title': response['items'][0]['snippet']['localized']['title'],
            'desc': response['items'][0]['snippet']['localized']['description']
        }
        return context

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        video_id = self.get_video_id(self.url)
        meta = self.get_meta(video_id)
        self.video_id = video_id
        self.title = meta['title']
        self.description = meta['desc']
        super(Videos, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )


class Event(AbstractClass):
    title = models.CharField(
        'Название',
        max_length=255,
    )
    body = models.TextField(
        'Текст эвента'
    )
    users = models.ManyToManyField(
        User,
        related_name='user_event',
        blank=True
    )

    class Meta:
        verbose_name = u'Эвенты'
        verbose_name_plural = u'эвенты'

    def __unicode__(self):
        return self.title


class Gallery(AbstractClass):
    title = models.CharField(
        'Название',
        max_length=255
    )
    img = ProcessedImageField(
        upload_to=get_image_gallery,
        processors=[ResizeToFill(980, 600)],
        format='PNG',
        options={'quality': 100},
        blank=True,
        null=True
    )
    preview = ImageSpecField(
        source='img',
        processors=[ResizeToFill(100, 100)],
        format='PNG',
        options={'quality': 60}
    )
    description = models.CharField(
        'Описание',
        max_length=255,
        blank=True,
        default=''
    )
    likes = models.ManyToManyField(
        User,
        related_name='user_like',
        blank=True
    )

    class Meta:
        verbose_name = u'Галлерея'
        verbose_name_plural = u'галлерея'

    def __unicode__(self):
        return self.title
