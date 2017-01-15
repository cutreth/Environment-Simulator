import RPi.GPIO as GPIO


def bool_to_out(state):

    if state:
        return GPIO.HIGH
    elif not state:
        return GPIO.LOW
