#!/usr/bin/python

from OSC import OSCServer
import sys
sys.path.append("/usr/local/pltn/rangeSensor")
import LED
import time
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
	#pSplit = path.split("/")
	#prog = pSplit[2]
	oscProg = args[0]
	pinValue = args[1]	
	
	if oscProg in gpioPins.keys():
		#search gpioPins dict for pin value. Exit when found
		for dictColor,gpioPin in gpioPins.iteritems():
			if oscProg == dictColor:
				break
		#set the pin color
		LED.setPinValue(gpioPin,pinValue)
	elif oscProg == 'allOn':
		LED.setColor(1,[1,1,1])
		LED.setColor(2,[1,1,1])
	elif oscProg == 'allOff':
		LED.allOff()
	else:
		pass	
		

def rpi(path, tags, args, source):
	print path
	print args

def pltn(path, tags, args, source):
	print path
	print args

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
oscSrv.addMsgHandler("/osc/led",led)
oscSrv.addMsgHandler("/osc/srvc",srvc)
oscSrv.addMsgHandler("/osc/pltn",pltn)
oscSrv.addMsgHandler("/osc/rpi",rpi)
#oscSrv.addMsgHandler("/led/tweet",tweet)


print "listening on port: %i" % OSCPort

try:
	while True:
		oscSrv.handle_request()

except KeyboardInterrupt:
	LED.allOff()
	print "Quit"
	oscSrv.close()
