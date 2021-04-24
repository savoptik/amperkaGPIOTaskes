import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

for i in [10, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24, 26]:
    GPIO.setup(i, GPIO.OUT)
    time.sleep(0.5)
    GPIO.output(i, GPIO.HIGH)

time.sleep(5)

for i in [10, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24, 26]:
    GPIO.output(i, GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup()

