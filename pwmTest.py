#import RPi.GPIO as GPIO
import RPIO
from RPIO import PWM
from time import sleep

dmaChannel = 1
PWM.setup()
PWM.init_channel(dmaChannel)

RPIO.setmode(RPIO.BOARD)
Motor1A = 16
Motor1B = 18
Motor1E = 22

RPIO.setup(Motor1A, RPIO.OUT)
RPIO.setup(Motor1B, RPIO.OUT)
RPIO.setup(Motor1E, RPIO.OUT)

print("Turning Motor on direction 1")
RPIO.output(Motor1A, RPIO.HIGH)
RPIO.output(Motor1B, RPIO.LOW)
RPIO.output(Motor1E, RPIO.HIGH)
PWM.add_channel_pulse(dmaChannel,Motor1E,0,50)
PWM.add_channel_pulse(dmaChannel,Motor1E,100,50)
sleep(2)
print("Changing velocity")
PWM.add_channel_pulse(dmaChannel,Motor1E,0,10)
PWM.add_channel_pulse(dmaChannel,Motor1E,100,10)
sleep(2)
PWM.clear_channel_gpio(dmaChannel,Motor1E)
PWM.cleanup()
RPIO.cleanup()
exit()


RPIO.output(Motor1E, RPIO.LOW)

sleep(1)

print("Turning Motor on direction 2")
RPIO.output(Motor1A, RPIO.LOW)
RPIO.output(Motor1B, RPIO.HIGH)

sleep(2)

servo.stop_servo(Motor1E)


sleep(2)

print("Turning Motor off")
RPIO.output(Motor1E, RPIO.LOW)

RPIO.cleanup()
