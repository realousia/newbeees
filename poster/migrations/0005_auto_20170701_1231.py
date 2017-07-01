# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0004_auto_20170701_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='honey',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
