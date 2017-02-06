from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from datetime import datetime, timedelta

import RPi.GPIO as GPIO
import models, do

from models import Reading


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
    return chart(request)


def chart(request):

    temp_data = [["'Instant'", "'Temp'", "'Temp T'", "'Temp D'"]]
    humid_data = [["'Instant'", "'Humid'", "'Humid T'", "'Humid D'"]]
    temp_add = []
    humid_add = []

    all_readings = Reading.objects.filter(instant__gte=(datetime.now() - timedelta(days=7)))

    for reading in all_readings:
        temp_add = ['new Date("' + str(reading.instant) + '")',
               str(reading.temp_val), 'undefined', 'undefined'
              ]
        humid_add = ['new Date("' + str(reading.instant) + '")',
               str(reading.humid_val), 'undefined', 'undefined'
              ]

        temp_data.append(temp_add)
        humid_data.append(humid_add)

        instant = str(reading)
        temp_gauge = str(reading.temp_val)
        humid_gauge = str(reading.humid_val)

    active_config = do.getConfig()
    end_time = datetime.now().date() + timedelta(days=1)
    start_time = end_time - timedelta(days=3)

    data = {'temp_data': temp_data, 'humid_data': humid_data, 'vals': {'instant': instant, 'end_time': end_time.isoformat(), 'start_time': start_time.isoformat(),
        'light_state': active_config.light_state, 'hour_morning': active_config.hour_morning, 'hour_night': active_config.hour_night,
        'temp': temp_gauge, 'temp_low': active_config.temp_low, 'temp_high': active_config.temp_high,
        'temp_state': active_config.temp_state, 'temp_low': active_config.temp_low, 'temp_high': active_config.temp_high,
        'humid': humid_gauge, 'humid_low': active_config.humid_low, 'humid_high': active_config.humid_high,
        'humid_state': active_config.humid_state, 'humid_low': active_config.humid_low, 'humid_high': active_config.humid_high}}

    return render_to_response('chart.html', data)
