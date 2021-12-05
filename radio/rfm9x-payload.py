# Payload Radio
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
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23

def reply(str):
	sending = bytes(str, 'utf-8')
	rfm9x.send(sending)

while True:
	packet = None
	packet = rfm9x.receive()

	if packet is None:
		continue
	else:
		sys.stdout = buffer = StringIO()

		prev_packet = str(packet, 'utf-8')

		# quit if we recv quit message, else run script
		if(prev_packet == "quit"):
			break
		else:
			print("[Payload] Running command : "+prev_packet)
			print(subprocess.getoutput("sudo "+prev_packet))

		# Send console output to base station and clear
		reply(buffer.getvalue())

		sys.stdout = sys.__stdout__
		print(buffer.getvalue())

	time.sleep(0.1)