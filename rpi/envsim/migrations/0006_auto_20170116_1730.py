# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envsim', '0005_auto_20170116_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='hour_morning',
            field=models.PositiveIntegerField(default=8, verbose_name='Morning Hour'),
        ),
        migrations.AddField(
            model_name='config',
            name='hour_night',
            field=models.PositiveIntegerField(default=18, verbose_name='Night Hour'),
        ),
        migrations.AddField(
            model_name='config',
            name='th_sensor',
            field=models.PositiveIntegerField(default=5, verbose_name='TH Sensor'),
        ),
        migrations.AlterField(
            model_name='config',
            name='humid_high',
            field=models.DecimalField(decimal_places=2, default=40, max_digits=4, verbose_name='Humid High'),
        ),
        migrations.AlterField(
            model_name='config',
            name='humid_low',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=4, verbose_name='Humid Low'),
        ),
        migrations.AlterField(
            model_name='config',
            name='temp_high',
            field=models.DecimalField(decimal_places=2, default=80, max_digits=4, verbose_name='Temp High'),
        ),
        migrations.AlterField(
            model_name='config',
            name='temp_low',
            field=models.DecimalField(decimal_places=2, default=60, max_digits=4, verbose_name='Temp Low'),
        ),
    ]
