import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
for i in [10, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24, 26]:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

input()

for i in [10, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24, 26]:
    GPIO.output(i, GPIO.LOW)

GPIO.cleanup()

