# Radio Changes
### Important
1. Convert most rfm9x functionality to its own class
  1. Send messages longer than 200 bytes
    - Define a standard of the message for doing so i.e. `'2,Message'` signifies there are 2 messages total and you need to wait for another
    - Make it apart fo the classes "send" function
  2. Structure to reduce code re-writing in the payload.py and base.py files
2. Add longer tests to test system capacity
3. Thorough logging
4. Integrate LED.py code into it
5. Attach 433 MHz antennas

### Backlog
1. Add support for more shells commands such as `cd` or `ls`
2. Create an arduino version for use with Windows computers

# Drone Changes
### Important
1. Get flight modes such as Alt. Hold working
### Backlog
2. GPS waypoint missions?

# Exploit Changes
### Important
### Backlog