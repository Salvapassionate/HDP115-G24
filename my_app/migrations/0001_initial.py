# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2023-05-14 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MisionEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mision', models.CharField(max_length=150)),
                ('tipo_mision', models.CharField(max_length=150)),
                ('empresa', models.CharField(max_length=150)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
