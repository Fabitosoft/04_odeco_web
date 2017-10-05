# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_soluciones', '0020_itemsolucion_marca_agua'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsolucion',
            name='marca_agua',
        ),
        migrations.AddField(
            model_name='itemsolucionimagen',
            name='marca_agua',
            field=models.PositiveIntegerField(choices=[(0, 'Ninguna'), (1, 'Blanca'), (2, 'Naranja')], default=2),
        ),
    ]