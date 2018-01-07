import math, datetime, time
import Adafruit_DHT

from models import Config, Reading


def sync():


    data = {}
    data = getStates(data)

    newReading(data)
    updateConfig(data)

    old_readings = Reading.objects.filter(instant__lt=(datetime.datetime.now() - datetime.timedelta(days=14)))
    old_readings.delete()


    return None


def logError():

    reading = Reading()
    reading.temp_val = 95
    reading.humid_val = 95
    reading.error = True
    reading.temp_state = False
    reading.humid_state = False
    reading.light_state = False
    reading.save()

    return None


def getStates(data):

    data = setLight(data)
    data = setTempHumid(data)

    return data


def setTempHumid(data):

    active_config = getConfig()
    data['temp_state'] = active_config.temp_state
    temp_low = active_config.temp_low
    temp_high = active_config.temp_high
    data['humid_state'] = active_config.humid_state
    humid_low = active_config.humid_low
    humid_high = active_config.humid_high
    humid_count = active_config.humid_count
    humid_length = active_config.humid_length

    data['temp_val'], data['temp_val2'], data['humid_val'], data['humid_val2'], data['error'] = readSensor()

    temp = (data['temp_val'] + data['temp_val2']) / 2
    humid = (data['humid_val'] + data['humid_val2']) / 2

    if temp <= temp_low:
        data['temp_state'] = True
    elif temp >= temp_high:
        data['temp_state'] = False

    if humid_count == 0:
        if humid <= humid_low:
            data['humid_state'] = True
            humid_count = 1
        elif humid >= humid_high:
            data['humid_state'] = False
    else:
        if humid_count == (humid_length + 1):
            data['humid_state'] = False
            humid_count = 0
        else:
            data['humid_state'] = True
            humid_count += 1

    updateHumidCount(humid_count)

    return data


def setLight(data):

    now = datetime.datetime.now().time()
    active_config = getConfig()
    morning = datetime.time(hour=active_config.hour_morning)
    night = datetime.time(hour=active_config.hour_night)

    if (morning <= now) & (now <= night):
        data['light_state'] = True
    else:
        data['light_state'] = False

    return data


def newReading(data):

    reading = Reading()
    reading.temp_val = data['temp_val']
    reading.temp_val2 = data['temp_val2']
    reading.humid_val = data['humid_val']
    reading.humid_val2 = data['humid_val2']
    reading.error = data['error']
    reading.temp_state = data['temp_state']
    reading.humid_state = data['humid_state']
    reading.light_state = data['light_state']
    reading.save()

    return None


def updateConfig(data):

    active_config = getConfig()
    active_config.temp_state = data['temp_state']
    active_config.humid_state = data['humid_state']
    active_config.light_state = data['light_state']
    active_config.save()

    return None


def getConfig():

    active_config = Config.objects.filter()[:1].get()
    return active_config


def updateHumidCount(value):

    active_config = getConfig()
    active_config.humid_count = value
    active_config.save()
    return None


def average(vals):

    avg = sum(vals)/len(vals)
    return avg


def stddev(vals):

    avg = average(vals)
    var = map(lambda x: (x - avg) ** 2, vals)
    dev = math.sqrt(average(var))
    return dev


def readSensor():

    active_config = getConfig()
    pin1 = active_config.temp_humid_sensor
    pin2 = active_config.temp_humid_sensor2
    error = False

    try:
        humid_val, temp_val = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, pin1)
    except Exception:
        humid_val = 11
        temp_val = 99
        error = True

    try:
        humid_val2, temp_val2 = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, pin2)
    except Exception:
        humid_val2 = 11
        temp_val2 = 99
        error = True

    try:
        temp_val = round(temp_val * 9 / 5 + 32, 1)
        humid_val = round(humid_val, 1)
    except Exception:
        humid_val = 11
        temp_val = 99
        error = True

    try:
        temp_val2 = round(temp_val2 * 9 / 5 + 32, 1)
        humid_val2 = round(humid_val2, 1)
    except Exception:
        humid_val2 = 11
        temp_val2 = 99
        error = True

    return temp_val, temp_val2, humid_val, humid_val2, error
