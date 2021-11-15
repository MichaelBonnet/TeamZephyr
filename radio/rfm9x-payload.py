# Payloa Radio (Receives first)
import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x
from os.path import exists
from io import StringIO
import os
import sys
import subprocess

# Configure stdout
#sys.stdout = buffer = StringIO()

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
		#print('[Radio Script] Received: ' + prev_packet)

		# quit if we recv quit message, else run script
		if(prev_packet == "quit"):
			break
		elif exists("./"+prev_packet):
			print("[Payload] Started remote script "+prev_packet)
			subprocess.call("sudo python3 "+prev_packet, shell=True)
		else:
			print("[Payload] File \""+prev_packet+"\" not found")
		
		# Send console output to base station and clear
		reply(buffer.getvalue())

		sys.stdout = sys.__stdout__
		print(buffer.getvalue())

		#os.system('clear')

	time.sleep(0.1)