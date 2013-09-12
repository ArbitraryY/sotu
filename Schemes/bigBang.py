#!/usr/bin/python

import sys
sys.path.append("/home/pltn/platoon/Modules")
from time import sleep
from Effects import Effects
from rsDistance import rsDistance

ef = Effects.Effects()

allOff     = [0,0,0]
startColor = [10,10,10]
endColor   = [255,255,255]
universeColors = [[28,30,68],[40,93,144],[123,32,144],[67,47,103]]
actionZone = [10,30]

while True:
    distance = rsDistance.measureAvg()
    print distance 
    
    if actionZone[0] <= distance <= actionZone[-1]:

        """fade in to brew
        """
        ef.fadeColor(allOff,startColor,1,0)

        """pulse at brewing period
        """
        ef.pulse(startColor,0.2,5,5,1)

        """pause before expansion
        """
        sleep(2)

        """accelerate to height
        """
        ef.fadeColor(startColor,endColor,49,0.01)

        """pause after expansion
        """
        sleep(5)

        #Fade to the universe colors after expansion
        ef.fadeColor(endColor,universeColors[0],1,0.05)

        #Rotate through universe colors
        ef.rotateColors(universeColors,1,1,0.001)

        #Fade out from the last color in the universe array
        ef.fadeColor(universeColors[-1],allOff,1,0)
   
        #measure distance again to see if should run playback again 
        distance = rsDistance.measureAvg()