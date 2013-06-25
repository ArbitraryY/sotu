#!/usr/bin/python

"""
@package ServiceMonitor.

This script queries the local system (every queryTime seconds) for a specified list of services
for their respective status and PIDs.  The statuses are then sent back to the control center OSC
Server
"""

import subprocess
from time import sleep
from OSC import OSCClient, OSCMessage

#List of PLTN dependent services
#srvcs       = ["ssh","pi-blaster","oscServer","agent","rangeSensor"]
srvcs       = ["ssh","pi-blaster","oscServer","pltnAgent","rangeSensor"]
pgrepOutput = []
queryTime   = 3 #Number of seconds between heartbeat check
OSCPort = 4567
OSCIP   = "localhost"

statusAddr = "/pltn/heartbeat" #heartbeat OSC address

#instantiate Client
srvcClient = OSCClient()
srvcClient.connect( (OSCIP, OSCPort) )

try:
    while True:
        #Get the RPis hostname
        h = subprocess.Popen(["hostname"], stdout=subprocess.PIPE)
        hOut, hErr = h.communicate()
        #hOut.rstrip('\n')
        #print "Host: " + hOut
        for srvc in srvcs:
            #Get the PIDs of each service in srvcs 
            p = subprocess.Popen(["pgrep", srvc], stdout=subprocess.PIPE)
            pOut, pErr = p.communicate()
            pOut.rstrip('\n')
            if pOut:
                #construct the OSC message
                oscMsg = OSCMessage(statusAddr)
                oscMsg.append(hOut.rstrip('\n'))
                oscMsg.append(srvc)
                oscMsg.append(1) #there was a service running
                oscMsg.append(pOut.rstrip('\n'))
                #send the OSC message to the Control center server
                srvcClient.send(oscMsg)
                #srvcClient.send( OSCMessage(statusAddr,[1,2,3]) )
                print "{0}: {1} " .format(srvc,pOut.rstrip('\n'))
                #for i in pgrepOutput:
                #    print i
            else:
                print "{0}: Stopped" .format(srvc)
        print "-------------------------"
        sleep(queryTime)

except KeyboardInterrupt:
        pass
