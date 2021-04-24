import RPi.GPIO as GPIO


def isPressed(btn, led):
    if GPIO.input(btn) == False:
        GPIO.output(led, GPIO.HIGH)
    else:
        GPIO.output(led, GPIO.LOW)


button1 = 3
button2 = 4


blueLeds = [10, 12, 14, 15, 17, 18, 21, 24, 26]
yellowLeds = [13, 16, 19]

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(blueLeds[:], GPIO.OUT)
GPIO.setup(yellowLeds[:], GPIO.OUT)

try:
    while True:
        isPressed(button1, blueLeds[:])
        isPressed(button2, yellowLeds[:])
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed.')