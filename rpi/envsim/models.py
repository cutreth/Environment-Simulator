from __future__ import unicode_literals

from django.db import models

import RPi.GPIO as GPIO


def bool_to_state(state):

    if state:
        return GPIO.HIGH
    elif not state:
        return GPIO.LOW


class Reading(models.Model):

    instant = models.DateTimeField('Instant', auto_now_add=True, unique=True)
    error = models.BooleanField('Error')

    temp_val = models.DecimalField('Temp Val', blank=True, null=True, max_digits=4, decimal_places=2)
    humid_val = models.DecimalField('Humid Val', blank=True, null=True, max_digits=4, decimal_places=2)

    temp_state = models.NullBooleanField('Temp State')
    humid_state = models.NullBooleanField('Humid State')
    light_state = models.NullBooleanField('Light State')

    def __str__(self):
        return str(self.instant.strftime('%Y-%m-%d %H:%M:%S'))

#for python manage.py makemigrations/migrate -> comment envisim/views.py calling setup()

class Config(models.Model):

    instant = models.DateTimeField('Instant', auto_now=True)

    temp_low = models.DecimalField('Temp Low', max_digits=4, decimal_places=2, default=60)
    temp_high = models.DecimalField('Temp High', max_digits=4, decimal_places=2, default=80)
    humid_low = models.DecimalField('Humid Low', max_digits=4, decimal_places=2, default=10)
    humid_high = models.DecimalField('Humid High', max_digits=4, decimal_places=2, default=40)

    humid_count = models.PositiveIntegerField('Humid Count', default=0)
    humid_length = models.PositiveIntegerField('Humid Length', default=10)
    hour_morning = models.PositiveIntegerField('Morning Hour', default=8)
    hour_night = models.PositiveIntegerField('Night Hour', default=18)

    temp_humid_sensor = models.PositiveIntegerField('Temp/Humid In', default=5)
    temp_pin = models.PositiveIntegerField('Temp Out', default=21)
    humid_pin = models.PositiveIntegerField('Humid Out', default=23)
    light_pin = models.PositiveIntegerField('Light Out', default=13)

    temp_state = models.BooleanField('Temp State')
    humid_state = models.BooleanField('Humid State')
    light_state = models.BooleanField('Light State')

    def save(self, *args, **kwargs):
        super(Config, self).save(*args, **kwargs)

        GPIO.setmode(GPIO.BCM)

        temp_out = bool_to_state(self.temp_state)
        temp_pin = self.temp_pin
        GPIO.output(temp_pin, temp_out)

        light_out = bool_to_state(self.light_state)
        light_pin = self.light_pin
        GPIO.output(light_pin, light_out)

        humid_out = bool_to_state(self.humid_state)
        humid_pin = self.humid_pin
        GPIO.output(humid_pin, humid_out)
