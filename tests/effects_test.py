#!/usr/bin/python


import sys
sys.path.append("/home/pltn/platoon/Modules")
from time import sleep
from LED import effects
from LED import CommonLED

ef = effects.effects()
cLED = CommonLED.CommonLED() 
#ef.pulse([0.7,0.6,0.8],0.001,10,10,0.07)
#ef.pulse([0.1,0.2,0.3],0.01,100,10,0.008)
#ef.pulse([1.0,1.0,1.0],0.001,100,10,0.01)
#ef.pulse([0.01,0.01,0.01],0.01,100,10,0.0008)

#print "%.2f" % cLED.aToD(137)

#ef.fadeColor([255,0,137],[0,0,24],1,0.001)
#ef.rotateColors([[28,30,68],[40,93,144],[255,255,255],[40,93,144],[123,32,144],[67,47,103]],1,1,0.001)
ef.rotateColors([[28,30,68],[40,93,144],[67,47,103]],1,1,0.001)
sleep(5)
cLED.allOff()