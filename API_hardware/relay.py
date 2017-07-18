
import platform



if platform.system() != 'Windows':
    import RPi.GPIO as GPIO
else:
    import API_hardware.GPIO_MOCK as GPIO

def init(pinlist):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    # loop through pins and set mode and state to 'low'
    for i in pinlist:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

def relayOn(i):
    try:
        GPIO.output(i, GPIO.LOW)


    except KeyboardInterrupt:
        # Reset GPIO settings
        GPIO.cleanup()

def relayOff(i):
    try:
        GPIO.output(i, GPIO.HIGH)


    except KeyboardInterrupt:
        # Reset GPIO settings
        GPIO.cleanup()


