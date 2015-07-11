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
	if (GPIO.input(WIRE) == 0): 	#Check if the wire has been touched
        GPIO.output(LED, True)		#If the wire has been touched, run this code
        time.sleep(2)
        GPIO.output(LED, False)

