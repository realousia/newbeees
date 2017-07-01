# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0002_honey_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=32)),
                ('info', models.CharField(max_length=128)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='flower',
            name='info',
            field=models.CharField(max_length=1024),
        ),
        migrations.RemoveField(
            model_name='flower',
            name='link',
        ),
        migrations.AlterField(
            model_name='flower',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AddField(
            model_name='flower',
            name='link',
            field=models.ManyToManyField(to='poster.Seed'),
        ),
    ]
