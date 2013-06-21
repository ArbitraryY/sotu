#!/usr/bin/python

from OSC import OSCServer
import sys
#sys.path.append("/usr/local/pltn/rangeSensor")
import LED
import time
import subprocess
import os
#import ledTwitter

gpioPins = {
			'r1':2,
			'g1':5,
			'b1':7,
			'r2':1,
			'g2':4,
			'b2':6,	
		}

OSCPort = 4567
OSCIP   = "0.0.0.0"

oscSrv = OSCServer((OSCIP,OSCPort))

def led(path, tags, args, source):
	oscProg = args[0]
	pinValue = args[1]	

	#check if first argument is a pin value
	if oscProg in gpioPins.keys():
		#search gpioPins dict for pin value. Exit when found
		for dictColor,gpioPin in gpioPins.iteritems():
			if oscProg == dictColor:
				break
		#set the pin color
		LED.setPinValue(gpioPin,pinValue)
	#Turn all LEDs on
	elif oscProg == 'allOn':
		LED.setColor(1,[1,1,1])
		LED.setColor(2,[1,1,1])
	#Turn all LEDs off
	elif oscProg == 'allOff':
		LED.allOff()
	else:
		pass	
		
def rpi(path, tags, args, source):
	print path
	print args
	cmd = args[0]
	if cmd == 'off':
		os.system("sudo shutdown -h now")
	else:
		pass

def srvc(path, tags, args, source):
	print path
	print args

#def tweet(path, tags, args, source):
	#ledTwitter.fadeTweet()
	#print path 
	#colors=[1,1,1]
	#allColors = [1,1,1,1,1,1]
	#LED.setColor(1,colors)	
	#LED.setColor(2,colors)	
	#LED.fadeOutThreading(0.01)	

#Message Handlers and Callback functions
oscSrv.addMsgHandler("/pltn/led",led)
oscSrv.addMsgHandler("/pltn/srvc",srvc)
oscSrv.addMsgHandler("/pltn/rpi",rpi)
#oscSrv.addMsgHandler("/led/tweet",tweet)


print "listening on port: %i" % OSCPort

try:
	while True:
		oscSrv.handle_request()

except KeyboardInterrupt:
	LED.allOff()
	print "Quit"
	oscSrv.close()
	
