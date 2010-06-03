#!/usr/bin/env python
import lightblue
import struct

spam = lightblue.socket()

datalog = open ("spam.log", "wt")

print "Please select the NXT brick"

(addr, port, name) = lightblue.selectservice()

spam.connect((addr, port))

print "Logging data..."

lenbuf = lambda b : sum(map(len, b))

while (1):
  spam_buffer = []
  try:
    spam_buffer.append(spam.recv(64))   # Always read 64 bytes at a time!
    while (lenbuf(spam_buffer) < 64) :
      spam_buffer.extend(spam.recv(64 - lenbuf(spam_buffer)))
    assert (lenbuf(spam_buffer) == 64)
    print 'Packet recieved has a lenght of: ', lenbuf(spam_buffer)
    spam_buffer = str(struct.unpack('2i3f2i3f6i', ''.join(spam_buffer))[:10])
    datalog.write (spam_buffer)
    datalog.write ("\n")
  except Exception, msg:
    print 'Due to something the data stream ended: ' , str(msg), lenbuf(spam_buffer)
    break
    
spam.close()
