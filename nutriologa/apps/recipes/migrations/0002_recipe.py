# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-19 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('image', models.ImageField(upload_to=b'recipes', verbose_name='Image')),
                ('description', models.TextField(verbose_name='Description')),
                ('category', models.CharField(choices=[(b'breakfast', b'Desayuno'), (b'collation', b'Colaciones'), (b'meal', b'Comidas'), (b'dinner', b'Cenas')], max_length=50, verbose_name='Category')),
            ],
        ),
    ]
