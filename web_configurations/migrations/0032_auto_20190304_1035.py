# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-04 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_configurations', '0031_generalconfiguration_texto_habeas_data_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalconfiguration',
            name='linkedin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='generalconfiguration',
            name='texto_habeas_data_en',
            field=tinymce.models.HTMLField(blank=True, default='Información Habeas Data', null=True, verbose_name='Habeas Data Ingles'),
        ),
    ]
