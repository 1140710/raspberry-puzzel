
import RPi.GPIO as GPIO

import time

import random
 
# Define pins for the LEDs

rood_pin = 17  # Eerste LED
blauw_pin = 27  # Tweede LED
groen_pin = 18
gele_pin = 21

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(rood_pin,GPIO.OUT)
    GPIO.setup(blauw_pin,GPIO.OUT)
    GPIO.setup(groen_pin,GPIO.OUT)
    GPIO.setup(gele_pin,GPIO.OUT)

    GPIO.output(rood_pin, GPIO.HIGH)
    GPIO.output(blauw_pin, GPIO.HIGH)
    # GPIO.output(gele_pin, GPIO.HIGH)


except KeyboardInterrupt:
    print("Cleaning up GPIO")
    GPIO.cleanup()

finally:
    GPIO.cleanup()

