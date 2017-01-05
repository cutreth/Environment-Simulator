import datetime


def check(pin):

    temperature = 0
    humidity = 0

    # humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, pin)

    if temperature < 70:
        temp = True
    else:
        temp = False

    return temp
