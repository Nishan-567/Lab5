import RPi.GPIO as gpio
import time
import math

GPIO.setmode(GPIO.BCM)

#1

pins = [] #pin numbers
f = 500 #frequency in Hz
#initialize all pins
for i in range(10):
	GPIO.setup(pin[i], GPIO.OUT)


dc_f = .2 # duty cycle B
t = time.time()
dc1 = (math.sin(2*math.pi*dc_f*t))**2 #pwm duty cycle


pwm = GPIO.PWM(pin[0], f)

pwm.start(dc1)

#2
phi = math.pi/11
dc2 = (math.sin(2*math.pi*dc_f*t - phi))**2

pwm = GPIO.PWM(pin[1], f)

pwm.start(dc2)