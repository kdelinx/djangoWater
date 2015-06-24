# coding: utf-8
import uuid, math
from datetime import date, datetime, timedelta
from django.db import models
from django.conf import settings
from core.models import AbstractClass
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill
from users.managers import UserManager


def get_water_avatar(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s%s' % (uuid.uuid4(), ext)
    return 'avatar/%s%s%s' % (filename[:1], filename[2:3], filename)

def get_water_photo(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s%s' % (uuid.uuid4(), ext)
    return 'photo/%s%s%s' % (filename[:1], filename[2:3], filename)

class Gender(AbstractClass):
    gender = models.CharField(
        max_length=7,
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.gender

class User(AbstractBaseUser, PermissionsMixin, AbstractClass):
    email = models.EmailField(
        'E-Mail',
        max_length=255,
        unique=True
    )
    login = models.CharField(
        'Логин',
        max_length=255,
        unique=True
    )
    # gender = models.ForeignKey(
    #     Gender,
    #     verbose_name='Пол',
    #     related_name='gender_user'
    # )
    first_name = models.CharField(
        'Фамилия',
        max_length=255
    )
    second_name = models.CharField(
        'Имя',
        max_length=255
    )
    third_name = models.CharField(
        'Отчество',
        max_length=255
    )
    avatar = ProcessedImageField(
        upload_to=get_water_avatar,
        processors=[ResizeToFill(250, 250)],
        format='PNG',
        options={'quality': 75},
        blank=True,
        null=True
    )
    address_home = models.TextField(
        'Домашний адрес',
    )
    address_work = models.TextField(
        'Рабочий адрес',
    )
    worktime = models.CharField(
        'График работы',
        max_length=255
    )
    traceroute = models.TextField(
        'Приблезительный маршрут'
    )
    favorite_place = models.TextField(
        'Места постоянного посещения'
    )
    photo_1 = ProcessedImageField(
        upload_to=get_water_photo,
        format='PNG',
        options={'quality': 80},
        default='',
        verbose_name='Фотография пользователя'
    )
    photo_2 = ProcessedImageField(
        upload_to=get_water_photo,
        format='PNG',
        options={'quality': 80},
        default='',
        verbose_name='Дополнительная фотография пользователя'
    )
    telephone = models.CharField(
        'Телефон',
        max_length=16
    )
    student_info = models.TextField(
        'Информация об учебе'
    )
    gentleman = models.BooleanField(
        'Джентельменское соглашение',
        default=True
    )
    birthday = models.DateField(
        'Дата рождения',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        default=True
    )
    is_admin = models.BooleanField(
        default=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'пользователи'

    def __unicode__(self):
        return self.login

    def get_full_name(self):
        return '%s %s %s' % (self.first_name, self.second_name, self.third_name)

    def get_short_name(self):
        return '%s. %s' % (self.first_name, self.second_name[0])

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_avatar_url(self):
        if self.avatar:
            avatar = self.avatar.url
        elif self.is_superuser or self.is_admin:
            avatar = settings.STATIC_URL + 'img/anoavatar.png'
        else:
            avatar = settings.STATIC_URL + 'img/unoavatar.png'
        return avatar

    def get_age(self):
        now = date.today()
        delta = now - self.birthday
        deltadays = delta.days
        deltayears = deltadays / 365.2425
        answer = int(math.floor(deltayears))
        return answer

    # def get_gender(self):
    #     if self.gender.id == 1:
    #         return u'Мужчина'
    #     else:
    #         return u'Женщина'

    @property
    def is_staff(self):
        return self.is_admin