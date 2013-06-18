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
def red(path, tags, args, source):
	ledTwitter.fadeRed()
def green(path, tags, args, source):
	ledTwitter.fadeGreen()
def blue(path, tags, args, source):
	ledTwitter.fadeBlue()
def scatter(path, tags, args, source):
	ledTwitter.scatter()

#Message Handlers and Callback functions
oscSrv.addMsgHandler("/led",ledActn)
oscSrv.addMsgHandler("/srvc",srvcActn)
oscSrv.addMsgHandler("/pltn",pltnActn)
oscSrv.addMsgHandler("/rpi",rpiActn)
oscSrv.addMsgHandler("/led/tweet",tweet)
oscSrv.addMsgHandler("/led/red",red)
oscSrv.addMsgHandler("/led/green",green)
oscSrv.addMsgHandler("/led/blue",blue)
oscSrv.addMsgHandler("/led/scatter",scatter)


print "listening on port" 
print OSCPort

try: 
	while True:
		oscSrv.handle_request()

except KeyboardInterrupt:
#	LED.allOff()
	print "Quit"
	ledTwitter.gpioClean()
	pass

oscSrv.close()
