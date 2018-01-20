from django.shortcuts import render_to_response
from datetime import datetime, timedelta

import RPi.GPIO as GPIO
import models
import do

from models import Reading


def setup():
    active_config = do.getConfig()

    GPIO.setmode(GPIO.BCM)

    temp_out = models.bool_to_state(active_config.temp_state)
    temp_pin = active_config.temp_pin
    GPIO.setup(temp_pin, GPIO.OUT, initial=temp_out)

    light_out = models.bool_to_state(active_config.light_state)
    light_pin = active_config.light_pin
    GPIO.setup(light_pin, GPIO.OUT, initial=light_out)

    humid_out = models.bool_to_state(active_config.humid_state)
    humid_pin = active_config.humid_pin
    GPIO.setup(humid_pin, GPIO.OUT, initial=humid_out)

setup()


def sync(request):
    do.sync()
    return chart(request)


def chart(request):
    temp_data = [["'Instant'", "'Temp Value'", "'Temp State'", "'Temp D'"]]
    humid_data = [["'Instant'", "'Humid Value'", "'Humid State'", "'Humid D'"]]
    temp_add = []
    humid_add = []

    all_readings = Reading.objects.all()
    reading_last = all_readings.last()

    for reading in all_readings:

        if reading.instant > reading_last.instant - timedelta(hours=96):

            count = 0
            temp = 0
            humid = 0

            if (reading.temp_val != None) & (reading.humid_val != None):
                count = count + 1
                temp = temp + reading.temp_val
                humid = humid + reading.humid_val

            if (reading.temp_val2 != None) & (reading.humid_val2 != None):
                count = count + 1
                temp = temp + reading.temp_val2
                humid = humid + reading.humid_val2

            if (reading.temp_val3 != None) & (reading.humid_val3 != None):
                count = count + 1
                temp = temp + reading.temp_val3
                humid = humid + reading.humid_val3

            if count == 0:
                count = 1
                temp = 50
                humid = 50

            temp = round(temp / count, 1)
            humid = round(humid / count, 1)

            temp_add = ['new Date("' + str(reading.instant) + '")',
                        str(temp), str(0 if reading.temp_state is False else 60), 'undefined'
                        ]
            humid_add = ['new Date("' + str(reading.instant) + '")',
                         str(humid), str(0 if reading.humid_state is False else 40), 'undefined'
                         ]

            temp_data.append(temp_add)
            humid_data.append(humid_add)

    instant = str(reading_last)
    temp_gauge = str(temp)
    humid_gauge = str(humid)

    temp_add = ['new Date("' + str(reading_last.instant + timedelta(days=1)) + '")', 'undefined', 'undefined', 'undefined']
    humid_add = ['new Date("' + str(reading_last.instant + timedelta(days=1)) + '")', 'undefined', 'undefined', 'undefined']
    temp_data.append(temp_add)
    humid_data.append(humid_add)

    active_config = do.getConfig()
    end_time = reading_last.instant + timedelta(hours=4)
    start_time = reading_last.instant - timedelta(hours=52)

    data = {'temp_data': temp_data, 'humid_data': humid_data,
            'vals': {'end_time': end_time.isoformat(), 'start_time': start_time.isoformat(),
                     'instant': instant, 'light_state': active_config.light_state,
                     'hour_morning': active_config.hour_morning, 'hour_night': active_config.hour_night,
                     'temp': temp_gauge, 'temp_state': active_config.temp_state,
                     'temp_low': active_config.temp_low, 'temp_high': active_config.temp_high,
                     'humid': humid_gauge, 'humid_state': active_config.humid_state,
                     'humid_low': active_config.humid_low, 'humid_high': active_config.humid_high,
                     }}

    return render_to_response('chart.html', data)
