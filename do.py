import platform

if "Windows" in platform.platform():
    import GPIO as GPIO
else:
    import RPi.GPIO as GPIO


def is_windows():

    if "Windows" in platform.platform():
        return True
    else:
        return False


def bool_to_out(state):

    if state:
        return GPIO.HIGH
    elif not state:
        return GPIO.LOW
