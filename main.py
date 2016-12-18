import platform
import time

import light

if "Windows" in platform.platform():
    import GPIO as GPIO
else:
    import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)


pin_light = 18
GPIO.setup(pin_light, GPIO.OUT)

'''
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
'''

try:
    while 1:
        if light.check():
            state_light = GPIO.HIGH
        else:
            state_light = GPIO.LOW
        GPIO.output(pin_light, state_light)
        time.sleep(5)

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
