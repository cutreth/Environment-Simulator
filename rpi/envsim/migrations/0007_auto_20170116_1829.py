# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envsim', '0006_auto_20170116_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='th_sensor',
        ),
        migrations.AddField(
            model_name='config',
            name='humid_pin',
            field=models.PositiveIntegerField(default=23, verbose_name='Humid Out'),
        ),
        migrations.AddField(
            model_name='config',
            name='light_pin',
            field=models.PositiveIntegerField(default=13, verbose_name='Light Out'),
        ),
        migrations.AddField(
            model_name='config',
            name='temp_humid_sensor',
            field=models.PositiveIntegerField(default=5, verbose_name='Temp/Humid In'),
        ),
        migrations.AddField(
            model_name='config',
            name='temp_pin',
            field=models.PositiveIntegerField(default=21, verbose_name='Temp Out'),
        ),
    ]
