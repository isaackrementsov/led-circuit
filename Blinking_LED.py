import RPi.GPIO as GPIO
import time


PIN = 18


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)


def blink_LED(pin, blink_time):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(blink_time)

    GPIO.output(pin, GPIO.LOW)
    time.sleep(blink_time)


for _ in range(20):
    blink_LED(PIN, 2)

    

