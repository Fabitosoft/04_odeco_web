# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 17:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_configurations', '0003_auto_20170925_1113'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LaEmpresa',
            new_name='LaEmpresaConfiguration',
        ),
        migrations.AlterModelOptions(
            name='laempresaconfiguration',
            options={'verbose_name': 'La Empresa'},
        ),
    ]
