## Node 1 will be used to send data
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

while command != 'quit':
	command = input('Send command: ')
	sending = bytes(command, 'utf-8')
	rfm9x.send(sending)
