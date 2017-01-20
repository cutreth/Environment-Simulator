import math, datetime, time
import Adafruit_DHT

from models import Config, Reading


def sync():

    data = fullSync()
    active_config = getConfig()

    while (data['humid_state'] is True) & (active_config.live_mode is False):
        partSync(data)
        data = fullSync()
        active_config = getConfig()

    return None


def fullSync():

    data = {}
    data = getStates(data)

    newReading(data)
    updateConfig(data)

    return data


def partSync(data):

    toggleLiveMode(True)

    while data['humid_state'] is True:
        time.sleep(30)
        data = getStates(data)

    toggleLiveMode(False)

    return None


def toggleLiveMode(state):

    active_config = getConfig()
    active_config.live_mode = state
    active_config.save()

    return None

def getStates(data):

    data = setTempHumid(data)
    data = setLight(data)

    return data


def setTempHumid(data):

    active_config = getConfig()
    data['temp_state'] = active_config.temp_state
    temp_low = active_config.temp_low
    temp_high = active_config.temp_high
    data['humid_state'] = active_config.humid_state
    humid_low = active_config.humid_low
    humid_high = active_config.humid_high

    data['temp_val'], data['humid_val'], data['error'] = readSensor()

    if data['temp_val'] <= temp_low:
        data['temp_state'] = True
    elif data['temp_val'] >= temp_high:
        data['temp_state'] = False

    if data['humid_val'] <= humid_low:
        data['humid_state'] = True
    elif data['humid_val'] >= humid_high:
        data['humid_state'] = False

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
    reading.humid_val = data['humid_val']
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


def average(vals):

    avg = sum(vals)/len(vals)
    return avg


def stddev(vals):

    avg = average(vals)
    var = map(lambda x: (x - avg) ** 2, vals)
    dev = math.sqrt(average(var))
    return dev


def readSensor(tries=4):

    active_config = getConfig()
    pin = active_config.temp_humid_sensor

    temp_count = 0
    humid_count = 0

    temp_list = []
    humid_list = []

    error = False

    for count in range(1, tries):

        humid_raw, temp_raw = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, pin)

        if (temp_raw > float(0)) & (humid_raw > float(0)):
            temp_list.append(temp_raw)
            humid_list.append(humid_raw)

    if (len(temp_list) != 0) & (len(humid_list) != 0):

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

    if (temp_count == 0) | (humid_count == 0):
        humid_sum, temp_sum = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, pin)
        temp_count = 1
        humid_count = 1
        error = True

    temp_val = temp_sum / temp_count
    humid_val = humid_sum / humid_count

    temp_val = round(temp_val * 9 / 5 + 32, 1)
    humid_val = round(humid_val, 1)

    return temp_val, humid_val, error
