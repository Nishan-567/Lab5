import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)

#1

pins = [2, 3] #pin numbers
f = 500 #frequency in Hz
#initialize all pins
for i in range(2):
	GPIO.setup(pins[i], GPIO.OUT)


dc_f = .2 # duty cycle B
t = time.time()
dc1 = (math.sin(2*math.pi*dc_f*t))**2 #pwm duty cycle


pwm = GPIO.PWM(pins[0], f)

pwm.start(dc1)

#2
phi = math.pi/11
dc2 = (math.sin(2*math.pi*dc_f*t - phi))**2

pwm = GPIO.PWM(pins[1], f)


pwm.start(dc2)



