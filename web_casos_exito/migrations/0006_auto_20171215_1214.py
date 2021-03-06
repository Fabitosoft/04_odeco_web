# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-15 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_casos_exito', '0005_auto_20171215_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndustriaCasoExito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('icono', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Industria',
                'verbose_name_plural': 'Industrias',
            },
        ),
        migrations.AlterField(
            model_name='casoexito',
            name='industria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mis_casos_exito', to='web_casos_exito.IndustriaCasoExito'),
        ),
    ]
