## Node 2 will be used to receive data
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
prev_packet = None

while prev_packet != 'quit':
	packet = None
	packet = rfm9x.receive()

	if packet is None:
		continue
	else:
		prev_packet = str(packet, 'utf-8')
		print('Received: ' + prev_packet)

	## important to prevent cpu overloading
	time.sleep(0.1)