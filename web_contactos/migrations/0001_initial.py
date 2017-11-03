# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteContacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('apellido', models.CharField(max_length=120)),
                ('correo', models.EmailField(max_length=120)),
                ('nro_contacto', models.CharField(max_length=120)),
                ('empresa', models.CharField(max_length=120)),
                ('cargo', models.CharField(blank=True, max_length=120, null=True)),
                ('pais', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'Contacto de Cliente',
                'verbose_name_plural': 'Contactos de Clientes',
            },
        ),
    ]