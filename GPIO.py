
BCM = "BCM"
BOARD = "BOARD"
OUT = "OUT"
IN = "IN"
LOW = "LOW"
HIGH = "HIGH"
PUD_UP = "UP"
PUD_DOWN = "DOWN"


def setmode(mode):
    print("Using Pin Number mode " + mode)
    return


def setup(pin, mode, pull_up_down = "NONE"):
    print("Pin " + str(pin) + " configured as " + mode + " " + pull_up_down)
    return


def output(pin, mode):
    print("Pin " + str(pin) + " output of " + mode)
    return


def input(pin):
    if pin % 2 == 0:
        print("Pin " + str(pin) + " input of LOW")
        output = False
    else:
        print("Pin " + str(pin) + " input of HIGH")
        output = True
    return output

def cleanup():
    print("Cleaning up")
    return
