#!/usr/bin/env python
import lightblue
import struct

spam = lightblue.socket()

datalog = open ("spam.log", "wt")

print "Please select the NXT brick"

(addr, port, name) = lightblue.selectservice()

spam.connect((addr, port))

print "Logging data..."

while (1):
  try: 
    spam_buffer = spam.recv(64)
    spam_buffer = str(struct.unpack('Ii56b', spam_buffer)[:2])
    datalog.write (spam_buffer)
    datalog.write ("\n" )
  except Exception, msg:
    print 'cazo, merda, cul ', str(msg)
    break
    
spam.close()
