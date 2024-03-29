import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x
import RPi.GPIO as GPIO
import subprocess
import logging
import datetime
import os
from utils.led import Led

def curr_time():
    return str(datetime.datetime.now())

def run_cmd(cmd):
    result = ""
    try:
        #ret = os.system(cmd)
        subprocess.run(cmd, check=True, shell=True)
        result = f"cmd '{cmd}' success {curr_time()}"
        logging.info(result)
        return (result, 0)
    except Exception as e:
        result = f"cmd '{cmd}' error: {e}  {curr_time()}"
        logging.error(result)
        return (result, -1)

def main():
    # init logging

    logging.basicConfig(filename="logs/payload.log", encoding="utf-8", level=logging.DEBUG)

    # init led
    led = Led()

    # init LoRa
    CS = DigitalInOut(board.CE1)
    RESET = DigitalInOut(board.D25)
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 433.0)
    rfm9x.tx_power = 23
    print("rfm9x initialized")
    logging.info(f"rmf9x initialized - {curr_time()}")

    recv = ""
    result = ("", 0)

    while recv != "quit":
        if(result[1] == 0):
        	led.blue()
        else:
        	led.red()
        recv = rfm9x.receive(with_ack=True, timeout=1000)
        recv = str(recv, "utf-8") if recv != None else ""
        
        if recv != "":
            led.green()
            result = run_cmd(recv)
            rfm9x.send_with_ack(result[0].encode("utf-8"))
            print(result[0])

if __name__ == "__main__":
    main()
