#!/usr/bin/python

import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')
 
# start an iterator thread so that serial buffer doesn't overflow
it = pyfirmata.util.Iterator(board)
it.start()
 
# set up pins
pin0=board.get_pin('a:0:i')             # A0 Input      (LM35)
#pin8=board.get_pin('d:8:i')             # D3 PWM Output (LED)
pin8=board.get_pin('d:8:i')             # D3 PWM Output (LED)
pin11=board.get_pin('d:11:p')             # D3 PWM Output (LED)

pin8.enable_reporting()
 
# IMPORTANT! discard first reads until A0 gets something valid
while pin0.read() is None:
    	print "passing"
	pass

def measure():
	start = time.time()
	#print pin0.board.pass_time(0.1)
	while str(pin8.read()) == 'False':
		start = time.time()
	#	print "Start time: %i" % start
	while str(pin8.read()) == 'True':
		stop = time.time()
	#	print "Stop time: %i" % stop
	elapsedTime = stop - start
	distance = (elapsedTime * 13512)/2
	#print "start time: %s " % start
	numMeasures = 60
	summ = 0
    	for i in range(numMeasures):
		dist = (pin0.read()*1024)/2
		summ += dist
	
	average = summ/len(range(numMeasures))
	board.pass_time(0.1)                  # pause 1 second
	#print "digi distance: %f" % distance
	print "Avg analog distance: %f" % average
	#print "raw value: %f" % pin0.read()
	
	return

try:
	while True:
		for i in range(1,10):
    			pin11.write(i/10.0)  # set D3 to 0, 10%, 20%, ... brightness
    			#print "PWM: %d" % i
    			board.pass_time(0.1)                  # pause 1 second
			#print (pin0.read() * 1000) / 9.766
			print measure()



except KeyboardInterrupt:
	print 'exiting'
	#pin11.write(0)                           # turn LED back off
	
board.exit()
