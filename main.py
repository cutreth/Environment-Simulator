import platform
import time

isWindows = False
if "Windows" in platform.platform():
    isWindows = True

if isWindows:
    import GPIO as GPIO
else:
    import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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

time.sleep(.25)
GPIO.cleanup()