# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envsim', '0004_config'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='humid_high',
            field=models.DecimalField(decimal_places=2, default=30, max_digits=4, verbose_name='Humid High'),
        ),
        migrations.AddField(
            model_name='config',
            name='humid_low',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=4, verbose_name='Humid Low'),
        ),
        migrations.AddField(
            model_name='config',
            name='temp_high',
            field=models.DecimalField(decimal_places=2, default=72, max_digits=4, verbose_name='Temp High'),
        ),
        migrations.AddField(
            model_name='config',
            name='temp_low',
            field=models.DecimalField(decimal_places=2, default=68, max_digits=4, verbose_name='Temp Low'),
        ),
    ]