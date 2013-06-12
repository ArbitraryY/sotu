#!/usr/bin/python

from OSC import OSCServer
import sys

sys.path.append("/home/nick/platoon/rangeSensor")
print sys.path
import LED


OSCPort = 4567
OSCIP   = "0.0.0.0"

oscSrv = OSCServer((OSCIP,OSCPort))

def red1(path, tags, args, source):
	print path 

print "listening on port" 
print OSCPort
while True:
	oscSrv.handle_request()
	oscSrv.addMsgHandler("/led/red1",red1)

	



oscSrv.server_close()
