import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x
import RPi.GPIO as GPIO
import logging
import datetime

def main():
    # init logging
    logging.basicConfig(filename="logs/base.log", level=logging.DEBUG)

    # init LoRa
    CS = DigitalInOut(board.CE1)
    RESET = DigitalInOut(board.D25)
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 433.0)
    rfm9x.tx_power = 23
    print("rfm9x initialized")

    sending = ""

    while sending != "quit":
        sending = input("[BASE]: ")
        rfm9x.send_with_ack(sending.encode("utf-8"))
        recv = rfm9x.receive(with_ack=True, timeout=90)
        recv = str(recv, "utf-8") if recv != None else ""
        print(f"> {recv}") 

if __name__ == "__main__":
    main()
