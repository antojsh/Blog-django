# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0005_auto_20160111_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.usuarios'),
        ),
    ]
