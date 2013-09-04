#!/usr/bin/python

import sys
sys.path.append("/home/pltn/platoon/Modules")
from time import sleep
from Effects import Effects
from rsDistance import rsDistance
from pltnGpio import pltnGpio

startColor = [0,0,255]
endColor   = [0,0,0]

ef = Effects.Effects()
pg = pltnGpio.pltnGpio()

#distance to activate scheme
actionZone = [10,30]

while True:
    distance = rsDistance.measureAvg()
    print distance 
    
    if actionZone[0] <= distance <= actionZone[-1]:
        ef.ledFlashFade(pg.getPin("b1"), 1, 0.05);
        ef.ledFlashFade(pg.getPin("b2"), 1, 0.05);