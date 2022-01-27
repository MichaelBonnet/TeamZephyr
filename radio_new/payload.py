import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x
import RPi.GPIO as GPIO

def main():
    # init LoRa
    CS = DigitalInOut(board.CE1)
    RESET = DigitalInOut(board.D25)
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 433.0)
    rfm9x.tx_power = 23
    print("rfm9x initialized")

    recv = ""

    while recv != "quit":
        recv = rfm9x.receive(with_ack=True, timeout=1000)
        recv = str(recv, "utf-8") if recv != None else ""
        
        #if recv != "":
        print(recv)

if __name__ == "__main__":
    main()
