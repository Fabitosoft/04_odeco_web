# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_empresa', '0011_galeriafotoempresaimagen_alt_seo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeriafotoempresaimagen',
            name='alt_seo',
            field=models.CharField(blank=True, default='', max_length=125, null=True),
        ),
    ]
