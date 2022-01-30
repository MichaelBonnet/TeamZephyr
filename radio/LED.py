import time, sys
import RPi.GPIO as GPIO

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

	def blue(self):
		self.off()
		self.blink(self.blue_pin)

	def yellow(self):
		self.off()
		self.blink(self.red_pin)
		self.blink(self.green_pin)

	def cyan(self):
		self.off()
		self.blink(self.green_pin)
		self.blink(self.blue_pin)

	def magenta(self):
		self.off()
		self.blink(self.red_pin)
		self.blink(self.blue_pin)
