# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import web_empresa.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_empresa', '0002_galeriafotoempresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='GaleriaFotoEmpresaImagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.PositiveIntegerField(default=0)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('imagen', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=web_empresa.models.GaleriaFotoEmpresaImagen.imagen_upload_to, verbose_name='Imagen Item Solución')),
                ('galeria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mis_imagenes', to='web_empresa.GaleriaFotoEmpresa')),
            ],
        ),
    ]
