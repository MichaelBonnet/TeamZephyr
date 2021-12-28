# Base Station Radio
# Team Zephyr
# Run script with 'python3 rfm9x-base.py' (may need sudo)

# Imports
import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x
import RPi.GPIO as GPIO

# LED Setup
GPIO.setmode(GPIO.BCM)
led_pin =  21
GPIO.setup(led_pin, GPIO.OUT)

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0) # Last argument is the frequency. LoRa supports 915 MHz and 868 MHz
rfm9x.tx_power = 23

# Variables initialized with default values
command = None
sending = True

# Main loop for sending data to payload
# Works as a remote shell via radio (LoRa module)
# Can send any linux command to the remote system, and prints output.
#
# Preset Commands:
# 'quit' : exits the loop and shuts down the script on BOTH sides (base station & payload)
while True:
    # If it's our turn to send (not currently listening for response)
	if sending:
		
		GPIO.output(led_pin, GPIO.HIGH)
        # Get input command from user
		command = input('[Base Station] Send command: ')
		GPIO.output(led_pin, GPIO.LOW)

		msg = bytes(command, 'utf-8')
        
        # Send the input to payload via radio
		rfm9x.send_with_ack(msg)

        # If the command was 'quit', break out of the loop (closes program)
		if(command == 'quit'):
			break

        # Set the 'sending' flag to false so we listen on our next loop iteration
		sending = False
        
    # If sending == false, we listen for {timeout} second(s) for any response from the payload
    # Default timeout is 1 second, can be changed below on line 48
	else:
		# Timeout in case message is not acknowledged
		timeout = 15   # [seconds]
		timeout_start = time.time()

        # While {timeout} second(s) have not passed, continue listening loop
		while (time.time() < timeout_start + timeout):
        
            # Clear anything we may have in the 'packet' variable
			packet = None
            
            # Attempt to recieve a message over radio (LoRa module) from payload station
			packet = rfm9x.receive()

            # Condition to check if our recieved packet contains any data
            # If it is empty, continue loop without any output
            # Else, decode the packet as a utf-8 encoded string, and print the output to console
			if packet is None:
				continue
			else:
				prev_packet = str(packet, 'utf-8')
				print(prev_packet, end="", flush=True)
		
        # Set the 'sending' flag back to true to return to sending mode
		sending = True
    
    # Short wait to optimize performance
	time.sleep(0.1)