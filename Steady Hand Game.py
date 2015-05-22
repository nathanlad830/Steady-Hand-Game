# Import Libraries
import RPi.GPIO as GPIO
import time

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set Pin Numbers
LED = 17
WIRE = 24

# Setup GPIO Output Channels
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(WIRE, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
	if (GPIO.input(WIRE) == 0):
        GPIO.output(LED, True)
        time.sleep(2)
        GPIO.output(LED, False)

