# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-29 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_soluciones', '0052_auto_20171229_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsolucion',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='itemsolucion',
            name='categoria_dos',
        ),
    ]
