import board
import adafruit_rgbled
import pwmio
import time

class Led:
    def __init__(self):
        red = pwmio.PWMOut(board.D17)
        green = pwmio.PWMOut(board.D27)
        blue = pwmio.PWMOut(board.D22)
        self.led = adafruit_rgbled.RGBLED(red, green, blue)
        
    def red(self):
        self.led.color = (255, 0, 0)

    def green(self):
        self.led.color = (0, 255, 0)

    def blue(self):
        self.led.color = (0, 0, 255)

    def yellow(self):
        self.led.color = (255, 128, 0)

    def orange(self):
        self.led.color = (255, 40, 0)
    
    def purple(self):
        self.led.color = (255, 0, 255)
    
    def cyan(self):
        self.led.color = (0, 128, 128)




def main():
    led = Led()

    led.red()
    time.sleep(1)

    led.green()
    time.sleep(1)

    led.blue()
    time.sleep(1)

    led.yellow()
    time.sleep(1)

    led.orange()
    time.sleep(1)
    
    led.purple()
    time.sleep(1)
    
    led.cyan()
    time.sleep(1)

if __name__ == "__main__":
    main()
