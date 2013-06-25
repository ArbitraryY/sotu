#!/usr/bin/python
"""@package OSCServer
Documentation for this module
"""

from OSC import OSCServer
import sys
import LED
import time
from subprocess import call
import time

#import ledTwitter

#dict for GPIO pins
gpioPins = {
			'r1':2,
			'g1':5,
			'b1':7,
			'r2':1,
			'g2':4,
			'b2':6,	
		}

#Define OSC server port and traceback IP
OSCPort = 4567
OSCIP   = "0.0.0.0"

#Instantiate server
oscSrv = OSCServer((OSCIP,OSCPort))
#instantiate time object
localtime = time.asctime( time.localtime(time.time()) )

def led(path, tags, args, source):
	"""
	Callback function to handle all LED functions.
		OSC Msg: /pltn/led <color+stripNum>|<LEDprogram> (0|1)
	"""
	oscProg  = args[0]
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
	"""
	Callback function to handle all RPi related functions
		OSC Msg: /pltn/rpi <function> <secretKey>
	"""
	#get the RPi command to run
	authzKey = "3681"
	cmd = args[0]
	key = args[1]
	#Check for proper command and authorization Key
	if cmd == 'off' and key == authzKey:
		print "{0}: RPi received shutdown command" .format(localtime)
		call(["sudo", "shutdown", "-h", "now"])
	else:
		print "{0}: \"{1} {2} {3}\" Not an allowed function/key combo" .format(localtime,path,cmd,key)

def srvc(path, tags, args, source):
	"""
	Callback function to handle all RPi related functions
		OSC Msg: /pltn/srvc <srvcName> start|stop
	"""
	#list of allowed services and values. Security to prevent rogue 
	#msgs being sent and started
	allowedSrvcs = ["pi-blaster","ssh","rangeSensor"]
	allowedCmds  = ["start","stop","status"]
	srvcName = args[0]
	value    = args[1]
	#check if this is an allowed command
	if srvcName in allowedSrvcs and value in allowedCmds:
		call(["sudo", "service", srvcName, value])
	else:
		print "{0}: \"{1} {2} {3}\" Not allowed" .format(localtime,path,srvcName,value) 

def heartbeat(path, tags, args, source):
	"""
	Callback function to process heartbeats from RPi. 
	"""
	print "---------------"
	print path
	print args[0]
	print args[1]
	print args[2]
	print args[3]
	
#def tweet(path, tags, args, source):
	#ledTwitter.fadeTweet()

#Message Handlers and Callback functions
oscSrv.addMsgHandler("/pltn/led",led)
oscSrv.addMsgHandler("/pltn/srvc",srvc)
oscSrv.addMsgHandler("/pltn/rpi",rpi)
oscSrv.addMsgHandler("/pltn/heartbeat",heartbeat)
#oscSrv.addMsgHandler("/led/tweet",tweet)

print "\n listening on port: %i" % OSCPort

try:
	while True:
		oscSrv.handle_request()

except KeyboardInterrupt:
	LED.allOff()
	print "Quit"
	oscSrv.close()