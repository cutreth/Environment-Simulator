import platform
import time

import light

if "Windows" in platform.platform():
    import GPIO as GPIO
else:
    import RPi.GPIO as GPIO

config_light = {}
config_light.update({'pin_out': 18})
config_light.update({'state': False})

config_water = {}
config_water.update({'pin_in': 19})
config_water.update({'pin_out': 20})
config_water.update({'state': False})

config_heat = {}
config_heat.update({'pin_in': 21})
config_heat.update({'pin_out': 22})
config_heat.update({'state': False})

GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(config_light['pin_out'], GPIO.OUT)
GPIO.setup(config_water['pin_in'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(config_water['pin_out'], GPIO.OUT)
GPIO.setup(config_heat['pin_in'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(config_heat['pin_out'], GPIO.OUT)

try:
    while 1:
        if light.check():
            state_light = GPIO.HIGH
        else:
            state_light = GPIO.LOW
        GPIO.output(config_light['pin_out'], state_light)
        time.sleep(60)

        '''
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)

        if GPIO.input(11):
            print("HIGH")
        else:
            print("LOW")

        if GPIO.input(14):
            print("HIGH")
        else:
            print("LOW")
        '''

except KeyboardInterrupt:
    GPIO.cleanup()
