# LionChief Controller
Script for controlling a LionChief train via Bluetooth

## About
LionChief trains can be controlled via Bluetooth(BLE, not classic) from a smart phone
using the LionChief app.  

Android has a bluetooth snooping feature. Using this with Wireshark, I was able
to figure out which GATT/ATT handle and value pairs to use to change speed, 
make noise, and more.  

All basic commands use handle 0x25 (UUID 08590f7e-db05-467e-8757-72f6faeb13d4).
Each command starts with 0x00, and ends with a checksum. Interestingly, the
train doesn't seem to actually -check- the checksum, but it's possibly logged
somewhere? I included the checksum calculation in the `LionChief` class, anyway.  

### Commands (excluding checksum and leading zero)
Horn start: `48 01`  
Horn stop : `48 00`  
Bell start: `47 01`  
Bell stop : `47 00`  
Speech    : `4d XX 00`  
Set speed : `45 <00-1f>`  
Forward   : `46 01`  
Reverse   : `46 02`  
Disconnect: `4b 0 0`  
Set master volume: `4b <00-07>`  
Set steam chuff volume: `4c <00-07>`  
Set horn volume/pitch:  `44 01 <00-0f> <fe-02>`  
Set bell volume/pitch: `44 02 <00-0f> <fe-02>`  
Set speech volume/pitch: `44 03 <00-0f> <fe-02>`  
Set engine volume/pitch: `44 04 <00-0f> <fe-02>`  
Set lights off: `51 00`  
Set lights on: `51 01`  

If the first parameter of the speech command is 0, the saying will be random.
Otherwise each value corresponds to a specific saying. Not sure what the
second parameter does.


## Troubleshooting
* Note that the speaker for at least some (if not all) Lionel trains is in the
tender; if it's not hooked up, the train will not make any sounds
* Some values like pitch are signed. Negative values are represented in 2's
compliment

## Usage
Demo usage can be found in `demo.py`. Make sure to change the MAC address

## Requirements
Tested with Python 3.9. Not expected to work outside Linux  
`pygatt`  
`pybluez`  

## Helpful Links for Future Projects
[The Practical Guide to Hacking BLE](https://blog.attify.com/the-practical-guide-to-hacking-bluetooth-low-energy/)  
[How to sniff Bluetooth traffic on Andorid](https://stackoverflow.com/questions/23877761/sniffing-logging-your-own-android-bluetooth-traffic)  
[About ATT and GATT](https://epxx.co/artigos/bluetooth_gatt.html)

## License
MIT
