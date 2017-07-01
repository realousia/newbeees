# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0005_auto_20170701_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='honeycomb',
            name='title',
            field=models.CharField(max_length=32, default=datetime.datetime(2017, 7, 1, 14, 53, 59, 554997, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
