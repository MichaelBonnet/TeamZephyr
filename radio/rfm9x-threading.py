import threading
import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x
import RPi.GPIO as GPIO



# Configure LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0) # Last argument is the frequency. LoRa supports 915 MHz and 868 MHz
rfm9x.tx_power = 23

def receive():
  while True:
    recv = rfm9x.receive(with_ack=True)
    if (recv is not None) and (recv is not 'quit'):
      recv = str(recv, 'utf-8')
      print('[RECV]>' + recv)
    elif(recv is 'quit'):
      break

def send():
  while True:
    msg = input('[SEND]>')
    msg = bytes(msg, 'utf-8')
    rfm9x.send_with_ack(msg)


t_receive = threading.Thread(target=receive)
t_send = threading.Thread(target=send)

t_receive.start()
t_send.start()

t_receive.join()



