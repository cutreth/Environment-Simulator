from django.shortcuts import render
from django.http import HttpResponse

import RPi.GPIO as GPIO
import models, do


def setup():

    active_config = do.getConfig()

    GPIO.setmode(GPIO.BCM)

    temp_out = models.bool_to_state(active_config.temp_state)
    temp_pin = active_config.temp_pin
    GPIO.setup(temp_pin, GPIO.OUT, initial=temp_out)

    humid_out = models.bool_to_state(active_config.humid_state)
    humid_pin = active_config.humid_pin
    GPIO.setup(humid_pin, GPIO.OUT, initial=humid_out)

    light_out = models.bool_to_state(active_config.light_state)
    light_pin = active_config.light_pin
    GPIO.setup(light_pin, GPIO.OUT, initial=light_out)

setup()


def sync(request):
    do.sync()
    response = HttpResponse('Sync successful')
    return response
