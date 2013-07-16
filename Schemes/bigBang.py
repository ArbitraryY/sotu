#!/usr/bin/python

import sys
sys.path.append("/home/pltn/platoon/Modules")
from time import sleep
from LED import effects

ef = effects.effects()

allOff = [0,0,0]
startColor = [0.01,0.01,0.01]
endColor   = [1.0,1.0,1.0]

#fade in to brew
ef.fadeUp(allOff,startColor,0.0008,0)

#pulse at brewing period
ef.pulse(startColor,0.2,5,10,0.0008)

#pause before expansion
sleep(2)

#accelerate to height
ef.fadeUp(startColor,endColor,0.04,0.05)

#pause after expansion
sleep(2)

#Pulse after height of explosion
ef.pulse(endColor,0.1,10,10,0.04)