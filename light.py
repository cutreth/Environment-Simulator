import datetime


def check(morning=8, night=18):

    morning = datetime.time(hour=morning)
    night = datetime.time(hour=night)
    now = datetime.datetime.now().time()

    if (morning < now) & (now < night):
        light = True
    else:
        light = False

    print(now)
    return light
