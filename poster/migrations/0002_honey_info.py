# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='honey',
            name='info',
            field=models.CharField(max_length=1024, blank=True, null=True),
        ),
    ]
