import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [13, 19, 16]

GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
dutyCycle = 50
pwm.start(dutyCycle)

try:
    while True:
        time.sleep(0.1)
        dutyCycle = dutyCycle + 10
        if dutyCycle > 100:
            dutyCycle = 0
        pwm.ChangeDutyCycle(dutyCycle)

except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed.')