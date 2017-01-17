import csv
import datetime
import math

import Adafruit_DHT


def check(pin, temp, humid, temp_low=60, temp_high=80, humid_low=10, humid_high=40):

    temp_count = 0
    humid_count = 0

    while temp_count == 0 & humid_count == 0:

        humidity1, temperature1 = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, pin)
        humidity2, temperature2 = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, pin)
        humidity3, temperature3 = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, pin)
        humidity4, temperature4 = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, pin)

        temp_list = [temperature1, temperature2, temperature3, temperature4]
        humid_list = [humidity1, humidity2, humidity3, humidity4]

        temp_avg = sum(temp_list) * 1.0 / 4
        humid_avg = sum(humid_list) * 1.0 / 4

        temp_var = map(lambda x: (x - temp_avg)**2, temp_list)
        humid_var = map(lambda x: (x - humid_avg)**2, humid_list)

        temp_var_avg = sum(temp_var) * 1.0 / 4
        humid_var_avg = sum(humid_var) * 1.0 / 4

        temp_dev = math.sqrt(temp_var_avg)
        humid_dev = math.sqrt(humid_var_avg)

        temp_sum = 0
        humid_sum = 0

        for x in temp_list:
            if abs(x - temp_avg) <= temp_dev:
                temp_sum += x
                temp_count += 1

        for x in humid_list:
            if abs(x - humid_avg) <= humid_dev:
                humid_sum += x
                humid_count += 1

    temperature = temp_sum / temp_count
    humidity = humid_sum / humid_count

    temperature = round(temperature * 9 / 5.0 + 32, 1)
    humidity = round(humidity, 1)

    print("Temp: " + str(temperature))
    print("Humid: " + str(humidity))

    if temperature < temp_low:
        temp = True
    elif temperature > temp_high:
        temp = False

    if humidity < humid_low:
        humid = True
    elif humidity > humid_high:
        humid = False

    fields = [datetime.datetime.now(), temperature, humidity, temp, humid]
    with open('log.txt', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

    return temp, humid
