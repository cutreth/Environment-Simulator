# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-02 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envsim', '0012_remove_config_live_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='humid_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Humid Count'),
        ),
    ]