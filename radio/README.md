# Please Read!!!
These two sample files (rfm9x_transmit and rfm9x_receive) are following from this [tutorial](https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi/raspberry-pi-wiring). This tutorial is **very**
thorough and goes over the basics of these modules. We need to make a class that more closely resembles what is happening in the tutorial. One where you can both receive and send data seemingly simultaneously. We will have to learn these modules fairly in depth because we will be sending larger than recommended amounts of data over the radio connection. Here is a link to the [RFM9X adafruit Library](https://github.com/adafruit/Adafruit_CircuitPython_RFM9x).

# Raspberry Pi Setup
1) For the payload Raspberry Pi be sure install Kali Linux (Insert version here)  
2) For the base station Raspberry Pi be sure to install Raspbian Lite (Insert Version Here)  
3) Be sure to install the libraries mentioned in the tutorial above so that the LoRa modules can be read by the raspberry pi and so that the correct python libraries are installed in order to run the code for both of the Raspberry Pi's.  
4) For the kali Linux raspberry pi, be sure to run this command 'edit/boot/config.txt - enable "dtparm=spi=on"' then reboot.  
5) Once the system is reboted then the scripts can be ran  
6) Optional*** if any libraries are missing then it should let you know, but be sure to install the missing libraries with 'apt-get install libraryname'  

# Running the scripts with our Raspberry Pis
1) SSH into the Raspberry Pi's (Insert IP addresses here and use port 22) The login for the kali linux pi is (Username: Kali / password: kali) and for the raspian pi it is (Username: pi  / Password: projectApt)  
2) Once logged in, navigate to the home directory for both of the pis using 'cd ~' and it will navigate you to the home directory where the scripts are at.
3) On the Kali be sure to run script with 'python3 rfm9x-payload.py' (may need sudo)
4) On the Raspbian pi be sure to run script with 'python3 rfm9x-base.py' (may need sudo)
5) Once both scripts are ran then you should be able to send commands from the base station Raspberry Pi and even use Bash commands to run scripts on the payload Raspberry Pi


## Future development
We need to integrate our payload and base station script into our exploitation and scanning script so that we can send and receive the information that we get from the penetration testing scripts back to the base station. We also need to be able to run commands from the base station so that they can be executed on the payload in order to execute the scanning script and the exploitation script whenever needed.
