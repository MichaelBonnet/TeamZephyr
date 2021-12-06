# Please Read!!!

These two sample files (rfm9x_transmit and rfm9x_receive) are following from this [tutorial](https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi/raspberry-pi-wiring). This tutorial is **very**
thorough and goes over the basics of these modules. We need to make a class that more closely resembles what is happening in the tutorial. One where you can both receive and send data seemingly simultaneously. We will have to learn these modules fairly in depth because we will be sending larger than recommended amounts of data over the radio connection. Here is a link to the [RFM9X adafruit Library](https://github.com/adafruit/Adafruit_CircuitPython_RFM9x).

# Raspberry Pi Setup

1) For the payload Raspberry Pi, install Kali Linux (Insert version here)
2) For the base station Raspberry Pi, install Raspbian Lite (Insert Version Here)
3) Install the libraries mentioned in the tutorial above so that the LoRa modules can be read by the Pis and so that the correct Python libraries are installed to run the code on both Raspberry Pis.
4) On the Pi running Kali Linux, be sure to run the following command, then reboot:
   1) `edit/boot/config.txt - enable "dtparm=spi=on"`
5) Once the system is rebooted, you can follow the instructions below.

# Running the scripts with our Raspberry Pis

1) SSH into the Raspberry Pi's (Insert IP addresses here and use port 22)
   1) Raspbian Lite (Controller):
      1) `ssh pi@192.168.50.128` (IP specific to our lab's network)
      2) Password: projectAPT
   2) Kali (Payload):
      1) `ssh kali@192.168.50.223` (IP specific to our lab's network)
      2) Password: kali
2) Once logged in, navigate to the home directory for both of the pis using 'cd ~' and it will navigate you to the home directory where the scripts are at, or where you can close the repository to get the scripts..
3) On the Kali Pi, run script `rfm9x-payload.py`:
      1) `python3 rfm9x-payload.py` (may need sudo)
5) On the Raspbian Pi, run script `rfm9x-base.py`:
      1) `python3 rfm9x-base.py` (may need sudo)
7) Once both scripts are running, you should be able to send commands from the base station Pi running Raspbian, including using Bash commands to run scripts on the payload Pi running Kali.

## Future development

We need to integrate our payload and base station script into our exploitation and scanning script so that we can send and receive the information that we get from the penetration testing scripts back to the base station. We also need to be able to run commands from the base station so that they can be executed on the payload in order to execute the scanning script and the exploitation script whenever needed.
