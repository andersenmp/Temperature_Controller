#Mock class for GPIO

BOARD = 1
BCM = 2
OUT = 1
IN = 1
HIGH = 1
LOW = 0


def setmode(a):
    print ("setmode GPIO",a)


def setup(a, b):
    print ("setup GPIO", a, b)


def output(a, b):
    print ("output GPIO", a, b)


def cleanup():
    print ("cleanup GPIO", a, b)


def setwarnings(flag):
    print ("setwarnings", flag)
