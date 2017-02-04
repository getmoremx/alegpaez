# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-26 04:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Recipe', 'verbose_name_plural': 'Recipes'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 1, 26, 4, 32, 9, 783544, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 1, 26, 4, 32, 13, 254900, tzinfo=utc)),
            preserve_default=False,
        ),
    ]