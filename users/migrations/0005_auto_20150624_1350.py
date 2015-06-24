# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150624_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.AddField(
            model_name='gender',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gender',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 24, 7, 50, 42, 657606, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
