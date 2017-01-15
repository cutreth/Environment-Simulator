import csv
import Adafruit_DHT


def check(pin, temp, humid, temp_low=70, temp_high=72, humid_low=20, humid_high=30):

    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, pin)
    temperature = round(temperature * 9 / 5.0 + 32, 1)
    humidity = round(humidity, 1)

    print("Temp: " + str(temperature))
    print("Humid: " + str(humidity))
    fields = [temperature, humidity]
    with open('log.txt', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

    if temperature < temp_low:
        temp = True
    elif temperature > temp_high:
        temp = False

    if humidity < humid_low:
        humid = True
    elif humidity > humid_high:
        humid = False

    return temp, humid
