#!/usr/bin/python

import sys
sys.path.append("/usr/local/pltn/rangeSensor/")
from LED import allOff

#turn all LEDs off
allOff()

print "Exiting from initLEDOff"

sys.exit()