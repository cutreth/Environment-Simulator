from __future__ import unicode_literals

from django.db import models


class Reading(models.Model):

    instant = models.DateTimeField('Instant', auto_now_add=True, unique=True)

    temp_val = models.DecimalField('Temp Val', blank=True, null=True, max_digits=4, decimal_places=2)
    humid_val = models.DecimalField('Humid Val', blank=True, null=True, max_digits=4, decimal_places=2)

    temp_state = models.NullBooleanField('Temp State')
    humid_state = models.NullBooleanField('Humid State')
    light_state = models.NullBooleanField('Light State')


class Config(models.Model):

    instant = models.DateTimeField('Instant', auto_now=True)

    temp_low = models.DecimalField('Temp Low', max_digits=4, decimal_places=2, default=68)
    temp_high = models.DecimalField('Temp High', max_digits=4, decimal_places=2, default=72)
    humid_low = models.DecimalField('Humid Low', max_digits=4, decimal_places=2, default=20)
    humid_high = models.DecimalField('Humid High', max_digits=4, decimal_places=2, default=30)

    temp_state = models.BooleanField('Temp State')
    humid_state = models.BooleanField('Humid State')
    light_state = models.BooleanField('Light State')
