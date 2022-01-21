import time, sys
import RPi.GPIO as GPIO

#TODO: add the self keyword used in redOn and redOff to the rest of the color function as used in those functions

class LED:
	def __init__(self):
		self.redPin = 11
		self.greenPin= 13
		self.bluePin= 15
	
	def blink(self, pin):
	    	GPIO.setwarnings(False)
	    	GPIO.setmode(GPIO.BOARD)
	    	GPIO.setup(pin, GPIO.OUT)
	    	GPIO.output(pin, GPIO.HIGH)
    
	def turnOff(self, pin):
	    	GPIO.setwarnings(False)
	    	GPIO.setmode(GPIO.BOARD)
	    	GPIO.setup(pin, GPIO.OUT)
	    	GPIO.output(pin, GPIO.LOW)
	  	
	def redOn(self):
	    	self.blink(self.redPin)

	def redOff(self):
	    	self.turnOff(self.redPin)

	def greenOn():
	    	blink(greenPin)

	def greenOff():
	    	turnOff(greenPin)

	def blueOn():
	    	blink(bluePin)

	def blueOff():
	    	turnOff(bluePin)

	def yellowOn():
	    	blink(redPin)
	    	blink(greenPin)

	def yellowOff():
	    	turnOff(redPin)
	    	turnOff(greenPin)

	def cyanOn():
		blink(greenPin)
		blink(bluePin)

	def cyanOff():
	    	turnOff(greenPin)
	    	turnOff(bluePin)

	def magentaOn():
	    	blink(redPin)
	    	blink(bluePin)

	def magentaOff():
	    	turnOff(redPin)
	    	turnOff(bluePin)

	def whiteOn():
	    	blink(redPin)
	    	blink(greenPin)
	    	blink(bluePin)

	def whiteOff():
	    	turnOff(redPin)
	    	turnOff(greenPin)
	    	turnOff(bluePin)
	

#Example code that calls the function
drone = LED()
drone.redOff()
	

	  	    	