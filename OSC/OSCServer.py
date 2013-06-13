#!/usr/bin/python

from OSC import OSCServer
import sys
sys.path.append("/usr/local/pltn/rangeSensor")
import LED
import re
import time
import ledTwitter

OSCPort = 4567
OSCIP   = "0.0.0.0"

oscSrv = OSCServer((OSCIP,OSCPort))

def ledActn(path, tags, args, source):
	#print path
	#print args
	regex = re.compile("\/led\/(.*)")
	r = regex.search(path)
	print r
	regex.match(path)
	# <_sre.SRE_Match object at 0xa4a20754936448d0>
	# List the groups found
	print r.groups()
	#print regex.findall(path)

def rpiActn(path, tags, args, source):
	print path
	print args

def pltnActn(path, tags, args, source):
	print path
	print args

def srvcActn(path, tags, args, source):
	print path
	print args

def tweet(path, tags, args, source):
	ledTwitter.fadeTweet()
	#print path 
	#colors=[1,1,1]
	#allColors = [1,1,1,1,1,1]
	#LED.setColor(1,colors)	
	#LED.setColor(2,colors)	
	#LED.fadeOutThreading(0.01)	

#Message Handlers and Callback functions
oscSrv.addMsgHandler("/led",ledActn)
oscSrv.addMsgHandler("/srvc",srvcActn)
oscSrv.addMsgHandler("/pltn",pltnActn)
oscSrv.addMsgHandler("/rpi",rpiActn)
oscSrv.addMsgHandler("/led/tweet",tweet)


print "listening on port" 
print OSCPort

while True:
	oscSrv.handle_request()

#except KeyboardInterrupt:
#	LED.allOff()
#	print "Quit"
oscSrv.close()
