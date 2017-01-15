import RPi.GPIO as GPIO
import time
import datetime

import do
import light
import temp

print("Starting setup")

config_light = {}
config_light.update({'pin_out': 13})
config_light.update({'initial': GPIO.LOW})

config_temp = {}
config_temp.update({'pin_in': 5})
config_temp.update({'pin_out': 21})
config_temp.update({'initial': GPIO.LOW})

config_humid = {}
config_humid.update({'pin_out': 23})
config_humid.update({'initial': GPIO.LOW})

GPIO.setmode(GPIO.BCM)
GPIO.setup(config_light['pin_out'], GPIO.OUT, initial=config_light['initial'])
GPIO.setup(config_temp['pin_out'], GPIO.OUT, initial=config_temp['initial'])
GPIO.setup(config_humid['pin_out'], GPIO.OUT, initial=config_humid['initial'])

state_temp = config_temp['initial']
state_humid = config_humid['initial']

print("Setup complete")

try:
    while 1:

        print(datetime.datetime.now())

        state_temp, state_humid = temp.check(config_temp['pin_in'], state_temp, state_humid)
        out_temp = do.bool_to_out(state_temp)
        GPIO.output(config_temp['pin_out'], out_temp)

        out_humid = do.bool_to_out(state_humid)
        GPIO.output(config_humid['pin_out'], out_humid)

        state_light = light.check()
        out_light = do.bool_to_out(state_light)
        GPIO.output(config_light['pin_out'], out_light)

        print("Temp: " + str(state_temp))
        print("Humid: " + str(state_humid))
        print("Light: " + str(state_light))

        time.sleep(30)


except KeyboardInterrupt:
    GPIO.cleanup()
