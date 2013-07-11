#!/usr/bin/python

import sys
sys.path.append("/usr/local/pltn/Modules")
from Pblstr import Pblstr

ALL_GPIO_PINS   = [2,1,5,4,7,6]

#Instantiate a Pblstr object
pb = Pblstr.Pblstr()

"""
set all GPIO to off
"""
for pin in ALL_GPIO_PINS:
    pb.write(pin,0)