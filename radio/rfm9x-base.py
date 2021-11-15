# Base Station Radio (Sends first)
import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x

# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23

command = None
sending = True

while True:

	if sending:
		command = input('[Base Station] Send command: ')
		msg = bytes(command, 'utf-8')
		rfm9x.send_with_ack(msg)

		if(command == 'quit'):
			break

		sending = False
	else:
		# Timeout in case message is not acknowledged
		timeout = 1   # [seconds]
		timeout_start = time.time()

		while (time.time() < timeout_start + timeout):
			packet = None
			packet = rfm9x.receive()

			if packet is None:
				continue
			else:
				prev_packet = str(packet, 'utf-8')
				print(prev_packet)
			
		sending = True

	time.sleep(0.1)