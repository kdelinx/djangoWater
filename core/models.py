# coding: utf-8
from django.db import models


class AbstractClass(models.Model):
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True

class Event(AbstractClass):
    title = models.CharField(
        'Название',
        max_length=255,
    )
    body = models.TextField(
        'Текст эвента'
    )

    class Meta:
        verbose_name = u'Эвенты'
        verbose_name_plural = u'эвенты'

    def __unicode__(self):
        return self.title



class Page(AbstractClass):
    page = models.CharField(
        'Название страницы(en)',
        max_length=255
    )
    title = models.CharField(
        'Заголовок',
        max_length=255
    )
    body = models.TextField(
        'Тело страницы'
    )

    class Meta:
        verbose_name = u'Страницы'
        verbose_name_plural = u'страницы'

    def __unicode__(self):
        return self.title


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
