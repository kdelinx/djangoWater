# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'E-Mail')),
                ('login', models.CharField(max_length=255, verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd')),
                ('first_name', models.CharField(max_length=255, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('second_name', models.CharField(max_length=255, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('third_name', models.CharField(max_length=255, verbose_name=b'\xd0\x9e\xd1\x82\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe')),
                ('avatar', imagekit.models.fields.ProcessedImageField(null=True, upload_to=users.models.get_water_avatar, blank=True)),
                ('address_home', models.TextField(verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbc\xd0\xb0\xd1\x88\xd0\xbd\xd0\xb8\xd0\xb9 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81')),
                ('address_work', models.TextField(verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x87\xd0\xb8\xd0\xb9 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81')),
                ('worktime', models.CharField(max_length=255, verbose_name=b'\xd0\x93\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd0\xba \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b')),
                ('traceroute', models.TextField(verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xb7\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xbc\xd0\xb0\xd1\x80\xd1\x88\xd1\x80\xd1\x83\xd1\x82')),
                ('favorite_place', models.TextField(verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x81\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xbf\xd0\xbe\xd1\x81\xd0\xb5\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('photo_1', imagekit.models.fields.ProcessedImageField(default=b'', upload_to=users.models.get_water_photo, verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f')),
                ('photo_2', imagekit.models.fields.ProcessedImageField(default=b'', upload_to=users.models.get_water_photo, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x84\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd1\x8f \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f')),
                ('telephone', models.CharField(max_length=16, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd')),
                ('student_info', models.TextField(verbose_name=b'\xd0\x98\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd0\xbe\xd0\xb1 \xd1\x83\xd1\x87\xd0\xb5\xd0\xb1\xd0\xb5')),
                ('gentleman', models.BooleanField(default=True, verbose_name=b'\xd0\x94\xd0\xb6\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x81\xd0\xba\xd0\xbe\xd0\xb5 \xd1\x81\xd0\xbe\xd0\xb3\xd0\xbb\xd0\xb0\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('birthday', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.ForeignKey(related_name='gender_user', verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb', to='users.Gender'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
    ]
