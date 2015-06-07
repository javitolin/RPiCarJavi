import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

orange = 3
green = 7
blue = 10
white = 11

GPIO.setup(orange, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(white, GPIO.OUT)

#GPIO.output(orange, GPIO.HIGH)
GPIO.output(green, GPIO.HIGH)
#GPIO.output(blue, GPIO.HIGH)
#GPIO.output(white, GPIO.HIGH)

sleep(5)

GPIO.cleanup()
