import time, sys
import RPi.GPIO as GPIO

#TODO: add the self keyword used in redOn and redOff to the rest of the color function as used in those functions

class LED:
	def __init__(self):
		self.red_pin = 11
		self.green_pin = 13
		self.blue_pin = 15
	
	def blink(self, pin):
	    	GPIO.setwarnings(False)
	    	GPIO.setmode(GPIO.BOARD)
	    	GPIO.setup(pin, GPIO.OUT)
	    	GPIO.output(pin, GPIO.HIGH)
    
	def off(self):
	    	GPIO.setwarnings(False)
	    	GPIO.setmode(GPIO.BOARD)
	    	GPIO.setup(self.red_pin, GPIO.OUT)
	    	GPIO.output(self.red_pin, GPIO.LOW)
	    	GPIO.setup(self.green_pin, GPIO.OUT)
	    	GPIO.output(self.green_pin, GPIO.LOW)
	    	GPIO.setup(self.blue_pin, GPIO.OUT)
	    	GPIO.output(self.blue_pin, GPIO.LOW)
	  	
	def red(self):
		self.off()
		self.blink(self.red_pin)

	def green(self):
		self.off()
		self.blink(self.green_pin)

	def blue():
	    	blink(blue_pin)

	def yellow():
	    	blink(red_pin)
	    	blink(green_pin)

	def cyan():
		blink(green_pin)
		blink(blue_pin)

	def magenta():
	    	blink(red_pin)
	    	blink(blue_pin)

#Example code that calls the function
drone = LED()
#drone.off()
drone.green()	

	  	    	