# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2023-06-02 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0013_auto_20230601_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreE', models.CharField(max_length=100)),
                ('direccionE', models.CharField(max_length=200)),
                ('correoE', models.EmailField(max_length=254)),
                ('telefonoE', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'my_app_empresas',
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUb', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('coordenadaX', models.DecimalField(decimal_places=6, max_digits=9)),
                ('coordenadaY', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
            options={
                'db_table': 'my_app_ubicaciones',
            },
        ),
    ]
