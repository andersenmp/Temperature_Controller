import time
import sys
import platform

#To run in my mac env
import random

this = sys.modules[__name__]

this.temp_sensor = ""


def init(w1_slave):
    this.temp_sensor = w1_slave


def temp_raw():

    f = open(this.temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp(scale):

    if platform.system() == 'Darwin':
        return random.randrange(-55, 150)

    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()
    temp_output = lines[1].find('t=')

    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output + 2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        if scale == 'F':
            return temp_f
        else:
            return format(temp_c, '.2f')



