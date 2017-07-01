# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0003_auto_20170701_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='seed',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seed',
            name='selfcontent',
            field=models.IntegerField(default=1),
        ),
    ]
