#!/usr/bin/python

from OSC import OSCServer
import sys
sys.path.append("/home/nick/platoon/rangeSensor")
#import LED
import re

OSCPort = 4567
OSCIP   = "0.0.0.0"

oscSrv = OSCServer((OSCIP,OSCPort))

def ledActn(path, tags, args, source):
	print path
	print args
	m = re.match('\/led\/(\w+)', path)
	print m.group(0)
	# = split(path)

def rpiActn(path, tags, args, source):
	print path
	print args

def pltnActn(path, tags, args, source):
	print path
	print args

def srvcActn(path, tags, args, source):
	print path
	print args

#Message Handlers and Callback functions
oscSrv.addMsgHandler("/led",ledActn)
oscSrv.addMsgHandler("/srvc",srvcActn)
oscSrv.addMsgHandler("/pltn",pltnActn)
oscSrv.addMsgHandler("/rpi",rpiActn)

print "listening on port" 
print OSCPort

while True:
	oscSrv.handle_request()

oscSrv.close()
