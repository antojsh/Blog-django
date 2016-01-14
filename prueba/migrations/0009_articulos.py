# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0008_auto_20160111_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='articulos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.usuarios')),
            ],
        ),
    ]