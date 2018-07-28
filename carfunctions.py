# Import GPIO module and associated functions, and refer to it as "GPIO" throughout code
import RPi.GPIO as GPIO
# Import time module and associated functions, and refer to it as "Time" throughout code
import time as Time


def setup():

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(11, GPIO.OUT)

    GPIO.setup(13, GPIO.OUT)

    GPIO.setup(15, GPIO.OUT)

    GPIO.setup(18, GPIO.OUT)


# EXERCISE 1 #

# Directions: Below, the code for defining the function Forward is given.
# The variable "num" is the number of seconds that your car will travel in the
# defined direction (HINT: Use Time.sleep). Define the function Backward, Right,
# and Left below the Forward function.
# -------------------------------- ENTER CODE HERE ------------------------------- #


# Define a new function called "Forward" that takes in variable "num"
def Forward():

    # Calls setup function to set up pins
    setup()

    # Print "Forward"

    # Set pin 11 output to False
    GPIO.output(11, False)
    # Set pin 13 output to True
    GPIO.output(13, True)
    # Set pin 15 output to False
    GPIO.output(15, False)
    # Set pin 18 output to True
    GPIO.output(18, True)
    # End function execution
    # Time.sleep(1)
    # GPIO.cleanup()

    return


def Backward():
    setup()
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, True)
    GPIO.output(18, False)

    # Time.sleep(1)
    # GPIO.cleanup()
    return


def Right():

    # Calls setup function to set up pins
    setup()

    # Print "Forward"

    # Set pin 11 output to False
    GPIO.output(11, False)
    # Set pin 13 output to True
    GPIO.output(13, True)
    # Set pin 15 output to False
    GPIO.output(15, True)
    # Set pin 18 output to True
    GPIO.output(18, False)
    # End function execution
    # Time.sleep(1)
    # GPIO.cleanup()
    return


def Left():

    # Calls setup function to set up pins
    setup()

    # Print "Forward"

    # Set pin 11 output to False
    GPIO.output(11, True)
    # Set pin 13 output to True
    GPIO.output(13, False)
    # Set pin 15 output to False
    GPIO.output(15, False)
    # Set pin 18 output to True
    GPIO.output(18, True)
    # End function execution
    # Time.sleep(1)
    # GPIO.cleanup()
    return


def Stop():

    # Calls setup function to set up pins
    setup()
    GPIO.output(11, False)
    # Set pin 13 output to True
    GPIO.output(13, False)
    # Set pin 15 output to False
    GPIO.output(15, False)
    # Set pin 18 output to True
    GPIO.output(18, False)
    # End function execution

    GPIO.cleanup()
    return

# ---------------------------------- END CODE ------------------------------------ #
