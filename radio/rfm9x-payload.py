# Payload Radio
# Team Zephyr
# Run script with 'python3 rfm9x-payload.py' (may need sudo)

# Imports
import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x
from os.path import exists
from io import StringIO
import sys
import subprocess

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0) # Last argument is the frequency. LoRa supports 915 MHz and 868 MHz
rfm9x.tx_power = 23

# Utiliy function to easily send replies back to base station
def reply(str):
    # Encodes message as utf-8 string
	sending = bytes(str, 'utf-8')
    # Sends the packet to base station
	rfm9x.send_with_ack(sending)

# Main loop for listening for messages from base station
while True:
    # Clear anything we may have in the 'packet' variable
    packet = None
    # Attempt to recieve a message over radio (LoRa module) from payload station
    packet = rfm9x.receive()
    
    # If we recieved nothing, continue loop
    # Else, we attempt to parse the recieved message and run a command
    if packet is None:
        continue
    else:
        # Change the standard output to 'buffer' variable
        sys.stdout = buffer = StringIO()

        # Decode the received 'packet'
        prev_packet = str(packet, 'utf-8')

		# Quit if we recieve 'quit' command, else run command
        if(prev_packet == "quit"):
            break
        else:
			# Run the command received, and print the output to the 'buffer' variable
            print("[Payload] Running command : "+prev_packet)
            temp = subprocess.getoutput("sudo "+prev_packet)
        
        if not (prev_packet == "ls" or "whoami"):
            time.sleep(3.0)
            
        print(temp)

        # Break buffer into smaller pieces (rfm9x/LoRa limitation)
        bufferString = buffer.getvalue()

        maxSize = 250
        fragments = [bufferString[i:i+maxSize] for i in range(0, len(bufferString), maxSize)]

		# Send buffer value to base station
        for output in fragments:
            reply(output)

        reply("BANANAS")
        
        # Reset the standard output to the console
        sys.stdout = sys.__stdout__
        
        # Print the value of the buffer in console
        print(buffer.getvalue())
    
    # Wait to optimize performance
    time.sleep(0.1)