import RPi.GPIO as GPIO
import time

import do
import light
import temp


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

GPIO.setmode(GPIO.BOARD)
GPIO.setup(config_light['pin_out'], GPIO.OUT, initial=config_light['initial'])
GPIO.setup(config_temp['pin_out'], GPIO.OUT, initial=config_temp['initial'])
GPIO.setup(config_humid['pin_out'], GPIO.OUT, initial=config_humid['initial'])

try:
    while 1:

        state_temp, state_humid = temp.check(config_temp['pin_in'])
        state_temp = do.bool_to_out(state_temp)
        GPIO.output(config_temp['pin_out'], state_temp)

        state_humid = do.bool_to_out(state_humid)
        GPIO.output(config_humid['pin_out'], state_humid)

        state_light = light.check()
        state_light = do.bool_to_out(state_light)
        GPIO.output(config_light['pin_out'], state_light)

        time.sleep(30)


except KeyboardInterrupt:
    GPIO.cleanup()
