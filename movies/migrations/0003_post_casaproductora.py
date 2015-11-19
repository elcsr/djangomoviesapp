# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20151119_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='CasaProductora',
            field=models.CharField(default=datetime.datetime(2015, 11, 19, 23, 19, 53, 488416, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
