
import platform

#To run in my mac env
import random

if platform.system() != 'Windows':
    import Adafruit_DHT
else:
    import API_hardware.Adafruit_DHT_MOCK


def readHumTemp(sensor, pin):
    if platform.system() == 'Windows':
        humidity = random.randrange(0,100)
        temperature = random.randrange(-10,50)
    else:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        return humidity, temperature



