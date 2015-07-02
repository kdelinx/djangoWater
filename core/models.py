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


class FAQ(AbstractClass):
    questions = models.CharField(
        u'Вопрос',
        max_length=180,
    )
    answer = models.TextField(
        u'Ответ',
        blank=True,
        default=''
    )
    published = models.BooleanField(
        u'Опубликовать ?',
        default=False
    )

    class Meta:
        verbose_name = u'FAQ'
        verbose_name_plural = u'faq'

    def __unicode__(self):
        return self.questions