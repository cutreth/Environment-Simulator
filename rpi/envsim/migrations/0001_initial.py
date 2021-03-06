# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instant', models.DateTimeField(auto_now_add=True, verbose_name='Instant')),
                ('temp_val', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Temp Val')),
                ('humid_val', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Humid Val')),
                ('temp_state', models.BooleanField(verbose_name='Temp State')),
                ('humid_state', models.BooleanField(verbose_name='Humid State')),
                ('light_state', models.BooleanField(verbose_name='Light State')),
            ],
        ),
    ]
