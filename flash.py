import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
    while True:
        time.sleep(0.05)
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(17, GPIO.LOW)
except KeyboardInterrupt:
    print('the programm vas stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('PIO cleanup completed.')
