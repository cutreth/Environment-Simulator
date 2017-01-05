import random

import do


def check(pin):

    if do.is_windows():
        humidity = random.randint(20,80)
        temperature = random.randint(50,90)
    else:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302,pin)

    if temperature < 70:
        temp = True
    else:
        temp = False

    if humidity <40:
        humid = True
    else:
        humid = False

    return temp, humid
