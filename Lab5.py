import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)

pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5] #pin numbers
f = 500 #frequency in Hz
dc_f = .2 # duty cycle B
phi = -1 * math.pi/11 #phi for phase shift

#initialize all pins
for i in range(10):
	GPIO.setup(pins[i], GPIO.OUT)
#set up pwm for all led
pwm = []
for p in pins:
	pwmCall = GPIO.PWM(p, f)
	pwm.append(pwmCall)
	pwmCall.start(0)

#input pin
input = 26
GPIO.setup(input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Define a threaded callback function:
def myCallback(pin):
	phi = -1 * math.pi/11 #switch direction

# Execute myCallback() if 26 goes HIGH:
GPIO.add_event_detect(input, GPIO.RISING, callback=myCallback, bouncetime=100)

try:
	while True:
		#index through pwn array with enumerate to use index for phase shift
		for (index, pwmLED) in enumerate(pwm):
			phaseShift = index * phi
			t = time.time()
			B = (math.sin(2*math.pi*dc_f*t - phaseShift))**2
			dc = B * 100
			pwmLED.ChangeDutyCycle(dc)

except KeyboardInterrupt:
	print('\nExiting')

pwm.stop()
GPIO.cleanup()
	


















