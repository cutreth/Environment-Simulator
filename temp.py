import Adafruit_DHT


def check(pin, cold=70, dry=40):

    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, pin)
    temperature * 9 / 5.0 + 32

    if temperature < cold:
        temp = True
    else:
        temp = False

    if humidity < dry:
        humid = True
    else:
        humid = False

    return temp, humid
