import math, datetime, time
import Adafruit_DHT

from models import Config, Reading


def average(vals):

    avg = sum(vals)/len(vals)
    return avg


def stddev(vals):

    avg = average(vals)
    var = map(lambda x: (x - avg) ** 2, vals)
    dev = math.sqrt(average(var))
    return dev


def getconfig():

    active_config = Config.objects.filter()[:1].get()
    return active_config


def checktime():

    now = datetime.datetime.now().time()
    active_config = getconfig()

    morning = datetime.time(hour=active_config.hour_morning)
    night = datetime.time(hour=active_config.hour_night)

    if (morning < now) & (now < night):
        light_state = True
    else:
        light_state = False

    return light_state


def readsensor(tries=4):

    temp_list = []
    humid_list = []

    active_config = getconfig()
    pin = active_config.temp_humid_sensor

    temp_count = 0
    humid_count = 0

    while temp_count == 0 & humid_count == 0:

        for count in range(1, tries):

            humid_raw, temp_raw = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, pin)

            if (temp_raw > float(0)) & (humid_raw > float(0)):
                temp_list.append(temp_raw)
                humid_list.append(humid_raw)

        temp_avg = average(temp_list)
        humid_avg = average(humid_list)

        temp_dev = stddev(temp_list)
        humid_dev = stddev(humid_list)

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

    temp_val = temp_sum / temp_count
    humid_val = humid_sum / humid_count

    temp_val = round(temp_val * 9 / 5 + 32, 1)
    humid_val = round(humid_val, 1)

    return temp_val, humid_val


def sync():

    humid_state = syncguts()

    while humid_state == True:
        time.sleep(15)
        humid_state = livechecks()
        if humid_state == True:
            syncguts()

    return None


def syncguts():

    active_config = getconfig()
    temp_state = active_config.temp_state
    temp_low = active_config.temp_low
    temp_high = active_config.temp_high
    humid_state = active_config.humid_state
    humid_low = active_config.humid_low
    humid_high = active_config.humid_high

    temp_val, humid_val = readsensor()

    if temp_val <= temp_low:
        temp_state = True
    elif temp_val >= temp_high:
        temp_state = False

    if humid_val <= humid_low:
        humid_state = True
    elif humid_val >= humid_high:
        humid_state = False

    light_state = checktime()

    reading = Reading()
    reading.temp_val = temp_val
    reading.humid_val = humid_val
    reading.temp_state = temp_state
    reading.humid_state = humid_state
    reading.light_state = light_state
    reading.save()

    active_config.temp_state = temp_state
    active_config.humid_state = humid_state
    active_config.light_state = light_state
    active_config.save()

    return humid_state


def livechecks():

    active_config = getconfig()
    humid_state = active_config.humid_state
    humid_low = active_config.humid_low
    humid_high = active_config.humid_high

    temp_val, humid_val = readsensor()

    if humid_val <= humid_low:
        humid_state = True
    elif humid_val >= humid_high:
        humid_state = False

    return humid_state
