# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_soluciones', '0038_itemsolucionvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsolucionvideo',
            name='video',
            field=models.CharField(default='hola', max_length=500),
            preserve_default=False,
        ),
    ]
