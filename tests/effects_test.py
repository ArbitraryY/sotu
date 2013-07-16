#!/usr/bin/python


import sys
sys.path.append("/home/pltn/platoon/Modules")
from time import sleep
from LED import effects

ef = effects.effects()

#ef.pulse([0.7,0.6,0.8],0.001,10,10,0.07)
#ef.pulse([0.1,0.2,0.3],0.01,100,10,0.008)
#ef.pulse([1.0,1.0,1.0],0.001,100,10,0.01)
#ef.pulse([0.01,0.01,0.01],0.01,100,10,0.0008)

ef.fadeUp([0.0,0.0,0.0],[0.5,0.5,0.3],0.01,0.01)

sys.exit()