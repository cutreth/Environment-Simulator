import platform
import time

import light
import temp

if "Windows" in platform.platform():
    import GPIO as GPIO
else:
    import RPi.GPIO as GPIO

config_light = {}
config_light.update({'pin_out': 16})
config_light.update({'initial': GPIO.HIGH})

config_temp = {}
config_temp.update({'pin_in': 11})
config_temp.update({'pull_res': GPIO.PUD_UP})
config_temp.update({'pin_out': 15})
config_temp.update({'initial': GPIO.HIGH})

GPIO.setmode(GPIO.BOARD)
GPIO.setup(config_light['pin_out'], GPIO.OUT, initial=config_light['initial'])
GPIO.setup(config_temp['pin_out'], GPIO.OUT, initial=config_temp['initial'])
GPIO.setup(config_temp['pin_in'], GPIO.IN, pull_up_down=config_temp['pull_res'])

try:
    while 1:
        if light.check():
            state_light = GPIO.HIGH
        else:
            state_light = GPIO.LOW
        GPIO.output(config_light['pin_out'], state_light)

        if temp.check(config_temp['pin_in']):
            state_temp = GPIO.HIGH
        else:
            state_temp = GPIO.LOW
        GPIO.output(config_temp['pin_out'], state_temp)



        time.sleep(60)


except KeyboardInterrupt:
    GPIO.cleanup()
