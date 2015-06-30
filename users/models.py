# coding: utf-8
import uuid, math
from datetime import date
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models import AbstractClass
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill
from users.managers import UserManager


def get_water_avatar(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return 'avatar/%s%s%s' % (filename[:1], filename[2:3], filename)


def get_water_photo(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return 'photo/%s%s%s' % (filename[:1], filename[2:3], filename)


class Gender(models.Model):
    gender = models.CharField(
        max_length=7,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = u'Пол'
        verbose_name_plural = u'пол'

    def __unicode__(self):
        return self.gender


class User(AbstractClass, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        u'E-Mail',
        max_length=255,
    )
    login = models.CharField(
        u'Логин',
        max_length=255,
        unique=True
    )
    gender = models.ForeignKey(
        Gender,
        verbose_name=u'Пол',
        null=True,
        blank=True
    )
    first_name = models.CharField(
        u'Фамилия',
        max_length=255
    )
    second_name = models.CharField(
        u'Имя',
        max_length=255
    )
    third_name = models.CharField(
        u'Отчество',
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
        u'Домашний адрес',
    )
    address_work = models.TextField(
        u'Рабочий адрес',
    )
    worktime = models.CharField(
        u'График работы',
        max_length=255
    )
    traceroute = models.TextField(
        u'Приблезительный маршрут'
    )
    favorite_place = models.TextField(
        u'Места постоянного посещения'
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
        u'Телефон',
        max_length=16
    )
    student_info = models.TextField(
        u'Информация об учебе'
    )
    gentleman = models.BooleanField(
        u'Джентельменское соглашение',
        default=True
    )
    birthday = models.DateField(
        u'Дата рождения',
        blank=True,
        null=True
    )
    score_kill = models.IntegerField(
        u'Количество убийств',
        default=0,
        blank=True,
        null=True
    )
    score_die = models.IntegerField(
        u'Количество смертей',
        default=0,
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
        return '%s %s %s' % (self.first_name, self.second_name, self.third_name)

    def get_full_name(self):
        return '%s %s %s' % (self.first_name, self.second_name, self.third_name)

    def get_short_name(self):
        return '%s %s.' % (self.second_name, self.first_name[0])

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

    def get_gender(self):
        if self.gender.id == 1:
            return u'Мужчина'
        else:
            return u'Женщина'

    @property
    def is_staff(self):
        return self.is_admin


class Static(AbstractClass):
    user = models.ForeignKey(
        User,
        related_name='user_static',
        verbose_name=u'Игрок'
    )
    killed = models.ManyToManyField(
        User,
        related_name='enemy_static',
        verbose_name=u'Убитые участники игроком'
    )
    number_lobby = models.SmallIntegerField(
        'Номер лобби',
        default=0
    )

    class Meta:
        verbose_name = u'Статистика игр'
        verbose_name_plural = u'статистика игр'

    def __unicode__(self):
        return '%s - %s' % (self.number_lobby, self.user.login)
