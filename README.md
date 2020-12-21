# LionChief
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

## Commands (excluding checksum and leading zero)
Horn start: `48 01`  
Horn stop : `48 00`  
Bell start: `47 01`  
Bell stop : `47 00`  
Speech    : `4d 00 00`  
Set speed : `45 <value>`  

I'm not sure why speech has room for two values

## Usage
Demo usage can be found in `demo.py`. Make sure to change the MAC address
