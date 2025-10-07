import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)

pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5] #pin numbers
f = 500 #frequency in Hz
dc_f = .2 # duty cycle B

#initialize all pins
for i in range(10):
	GPIO.setup(pins[i], GPIO.OUT)
#set up pwm for all led
pwm = []
for p in pins:
	pwmCall = GPIO.PWM(p, f)
	pwm.append(pwmCall)
	pwmCall.start(0)

try:
	while True:
		for (index, pwmLED) in enumerate(pwm):
			phi = math.pi/11
			phaseShift = i * phi
			t = time.time()
			B = (math.sin(2*math.pi*dc_f*t - phi))**2
			dc = B * 100
			pwm.ChangeDutyCycle(dc)

except KeyboardInterrupt:
	print('\nExiting')

pwm.stop()
GPIO.cleanup()
	













