import platform
import time

import do
import light
import temp

if "Windows" in platform.platform():
    import GPIO as GPIO
else:
    import RPi.GPIO as GPIO

config_light = {}
config_light.update({'pin_out': 'light_out'})
config_light.update({'initial': GPIO.LOW})

config_temp = {}
config_temp.update({'pin_in': 'temp_in'})
config_temp.update({'pull_res': GPIO.PUD_UP})
config_temp.update({'pin_out': 'temp_out'})
config_temp.update({'initial': GPIO.LOW})

config_humid = {}
config_humid.update({'pin_out': 'humid_out'})
config_humid.update({'initial': GPIO.LOW})

GPIO.setmode(GPIO.BOARD)
GPIO.setup(config_light['pin_out'], GPIO.OUT, initial=config_light['initial'])
GPIO.setup(config_temp['pin_out'], GPIO.OUT, initial=config_temp['initial'])
GPIO.setup(config_temp['pin_in'], GPIO.IN, pull_up_down=config_temp['pull_res'])

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

        time.sleep(5)


except KeyboardInterrupt:
    GPIO.cleanup()
