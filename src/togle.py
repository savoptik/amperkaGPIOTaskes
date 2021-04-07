import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)

leds = [13, 19, 16]

GPIO.setup(24, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.output(10, GPIO.HIGH)

try:
    while True:
        button = not GPIO.input(2)
        for i in leds:
            GPIO.output(i, button)
        GPIO.output(24, not button)
except KeyboardInterupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.output(10, GPIO.LOW)
    GPIO.cleanup()
    print('GPIO cleanup completed')