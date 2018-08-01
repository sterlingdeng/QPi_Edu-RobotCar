
import RPi.GPIO as GPIO

import time as Time


def setup():

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(11, GPIO.OUT)

    GPIO.setup(13, GPIO.OUT)

    GPIO.setup(15, GPIO.OUT)

    GPIO.setup(18, GPIO.OUT)

def Forward():

    setup()
    GPIO.output(11, False)
 
    GPIO.output(13, True)

    GPIO.output(15, False)
 
    GPIO.output(18, True)

    return


def Backward():
    setup()
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, True)
    GPIO.output(18, False)

    return


def Right():

    setup()

    GPIO.output(11, False)

    GPIO.output(13, True)

    GPIO.output(15, True)

    GPIO.output(18, False)

    return


def Left():

    setup()

    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(18, True)

    return


def Stop():


    setup()
    GPIO.output(11, False)

    GPIO.output(13, False)
 
    GPIO.output(15, False)

    GPIO.output(18, False)


    GPIO.cleanup()
    return


