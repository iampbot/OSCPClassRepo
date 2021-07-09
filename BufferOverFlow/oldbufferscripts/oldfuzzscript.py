#!/usr/bin/python

import socket,sys

buffer=["A"]
counter=500
while len(buffer) <= 1:
        buffer.append("A"*counter)
        counter=counter+500 #increment by 100

try:
    for string in buffer:
        print "Fuzzing App with %s bytes" % len(string)
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect=s.connect(('127.0.0.1', 31337))
        s.recv(1024)
        s.send(string + '\r\n')
        s.close()

except:
    print "Could not connect to application, you might have crashed it"
