# Isaac Krementsov
# 3/8/2020
# Introduction to Systems Engineering
# Blinking LED - Controls two blinking LED lights

import RPi.GPIO as GPIO
import time


# GPIO pin numbers where the red and yellow LED circuits are connected
RED_PIN = 18
YELLOW_PIN = 24


# Set the GPIO header board to Broadcom Model setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup the two pins, connected to the red and yellow LEDs, for output
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)


# Blink the two LEDs for a period of time in an alternating pattern
def blink_LED(red_pin, yellow_pin, blink_time):
    # Set the power output to high for the red LED circuit and low for the yellow
    GPIO.output(red_pin, GPIO.HIGH)
    GPIO.output(yellow_pin, GPIO.LOW)
    # Force the program to wait before switching the lights
    time.sleep(blink_time)

    # Switch the power settings for the red and yellow circuits
    GPIO.output(red_pin, GPIO.LOW)
    GPIO.output(yellow_pin, GPIO.HIGH)
    # Wait before running the method again
    time.sleep(blink_time)


# Blink the LEDs 20 times
for _ in range(20):
    # Run the blink_LED function to blink the lights for 2 seconds
    blink_LED(RED_PIN, YELLOW_PIN, 2)

# Shut off the yellow light, since it would still be on otherwise
GPIO.output(YELLOW_PIN, GPIO.LOW)
