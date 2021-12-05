# Please Read!!!
These two sample files (rfm9x_transmit and rfm9x_receive) are following from this [tutorial](https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi/raspberry-pi-wiring). This tutorial is **very**
thorough and goes over the basics of these modules. We need to make a class that more closely resembles what is happening in the tutorial. One where you can both receive and send data seemingly simultaneously. We will have to learn these modules fairly in depth because we will be sending larger than recommended amounts of data over the radio connection. Here is a link to the [RFM9X adafruit Library](https://github.com/adafruit/Adafruit_CircuitPython_RFM9x).

## Future development
We need to integrate our payload and base station script into our exploitation and scanning script that we can send and receive the information that we get from the penetration testing scripts back to the base station. We also need to be able to run commands from the base station so that they can be executed on the payload in order to execute the scanning script and the exploitation script whenever needed.
