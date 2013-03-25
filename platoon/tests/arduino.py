#!/usr/bin/python

import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')
 
# start an iterator thread so that serial buffer doesn't overflow
it = pyfirmata.util.Iterator(board)
it.start()
 
# set up pins
#pin0=board.get_pin('a:0:i')             # A0 Input      (LM35)
#pin8=board.get_pin('d:8:i')             # D3 PWM Output (LED)
pin8=board.get_pin('d:8:i')             # D3 PWM Output (LED)
pin11=board.get_pin('d:11:p')             # D3 PWM Output (LED)

pin8.enable_reporting()
 
# IMPORTANT! discard first reads until A0 gets something valid
#while pin0.read() is None:
#    pass

def measure():
	start = time.time()
	while pin8.read() == 'False':
		start = time.time()
	while pin8.read() == 'True':
		stop = time.time()
	elapsedTime = stop - start
	distance = (elapsedTime * 13512)/2
	return distance

while 1:
	for i in range(1,10):
    		pin11.write(i/10.0)                  # set D3 to 0, 10%, 20%, ... brightness
    	#	print "PWM: %d" % i
    		board.pass_time(0.1)                  # pause 1 second
	#print (pin0.read() * 1000) / 9.766
	print measure()


pin11.write(0)                           # turn LED back off

#except KeyboardInterrupt
#	print 'exiting'
	
board.exit()
