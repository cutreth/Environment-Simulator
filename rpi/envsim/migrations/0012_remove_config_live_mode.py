# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 01:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envsim', '0011_auto_20170120_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='live_mode',
        ),
    ]
