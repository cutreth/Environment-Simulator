import platform
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
GPIO.setup(12, GPIO.IN)

GPIO.output(18, GPIO.HIGH)
GPIO.output(18, GPIO.LOW)

if GPIO.input(12):
    print("HIGH")
else:
    print("LOW")

