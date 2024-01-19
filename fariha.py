
import RPi.GPIO as GPIO

import time

import random
 
# Define pins for the LEDs

led1_pin = 17  # Eerste LED

led2_pin = 27  # Tweede LED
 
# Define pins for the buttons

button1_pin = 23

button2_pin = 24
 
# Define pins for the 7-segment display

segment_pins = {

    'a': 12,

    'b': 16,

    'c': 13,

    'd': 19,

    'e': 26,

    'f': 21,

    'g': 20

}
 
# Number to segments mapping (assuming common cathode display)

numbers = {

    0: ['a', 'b', 'c', 'd', 'e', 'f'],

    1: ['b', 'c'],

    2: ['a', 'b', 'd', 'e', 'g'],

    3: ['a', 'b', 'c', 'd', 'g'],

    4: ['b', 'c', 'f', 'g'],

    5: ['a', 'c', 'd', 'f', 'g'],

    6: ['a', 'c', 'd', 'e', 'f', 'g'],

    7: ['a', 'b', 'c'],

    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],

    9: ['a', 'b', 'c', 'd', 'f', 'g']

}
 
# Setup GPIO mode

GPIO.setmode(GPIO.BCM)
 
# Setup pins for LEDs

GPIO.setup(led1_pin, GPIO.OUT)

GPIO.setup(led2_pin, GPIO.OUT)
 
# Setup pins for buttons

GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
# Setup pins for the 7-segment display

for pin in segment_pins.values():

    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, GPIO.LOW)  # Assuming a common cathode display
 
# Function to display numbers on the 7-segment display

def display_number(number):

    # Turn off all segments

    for pin in segment_pins.values():

        GPIO.output(pin, GPIO.LOW)  # Assuming a common cathode display
 
    # Turn on the required segments for the given number

    for segment in numbers.get(number, []):

        GPIO.output(segment_pins[segment], GPIO.HIGH)  # Assuming a common cathode display
 
# Function to run the "Simon Says" game

def simon_says_game(led_pins, button_pins, display_function, rounds=1):

    pattern = []  # This will store the pattern of LEDs

    # Display a random pattern

    for _ in range(rounds):

        led = random.choice(led_pins)

        GPIO.output(led, GPIO.HIGH)

        pattern.append(led)

        time.sleep(1)

        GPIO.output(led, GPIO.LOW)

        time.sleep(0.5)
 
    time.sleep(1)  # Pause before starting the player's turn
 
    # Now the player needs to repeat the pattern

    for led in pattern:

        start_time = time.time()

        time_remaining = 10

        while time_remaining >= 0:

            display_function(time_remaining)  # Update the 7-segment display with the time left

            if GPIO.input(button_pins[0]) == GPIO.LOW and led == led_pins[0]:

                print("Correct button 1 pressed!")

                break

            elif GPIO.input(button_pins[1]) == GPIO.LOW and led == led_pins[1]:

                print("Correct button 2 pressed!")

                break

            time.sleep(0.1)

            time_remaining = 10 - int(time.time() - start_time)
 
        if time_remaining <= 0:

            print("Time's up! Game over.")

            return False  # The player was too slow

        else:

            GPIO.output(led, GPIO.HIGH)

            time.sleep(0.5)

            GPIO.output(led, GPIO.LOW)

            time.sleep(0.5)
 
    print("Well done!")

    return True  # The player was successful
 
# Main program

try:

    while True:

        success = simon_says_game([led1_pin, led2_pin], [button1_pin, button2_pin], display_number, rounds=3)

        if not success:

            print("Game over. Let's try again!")

            time.sleep(2)
 
except KeyboardInterrupt:

    print("Program stopped by user")
 
finally:

    GPIO.cleanup()  # Clean up GPIO to ensure it is reset
    #okok
 
