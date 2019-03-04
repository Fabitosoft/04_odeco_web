# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-03 13:59
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_configurations', '0029_casosexitoconfiguration_descripcion_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalconfiguration',
            name='texto_habeas_data',
            field=tinymce.models.HTMLField(blank=True, default='Información Habeas Data', null=True, verbose_name='Habeas Data'),
        ),
    ]