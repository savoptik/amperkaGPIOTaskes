import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)

leds = [13, 19, 16]

for i in  leds:
    GPIO.setup(i, GPIO.OUT)

try:
    while True:
        button = not GPIO.input(2)
        for i in leds:
            GPIO.output(i, button)

except KeyboardInterupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')