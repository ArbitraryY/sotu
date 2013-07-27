#!/usr/bin/python

import sys
sys.path.append("/home/pltn/platoon/Modules")
from time import sleep
from LED import effects
from rsDistance import rsDistance
from pltnGpio import pltnGpio

startColor = [255,0,0]
endColor   = [0,0,0]

ef = effects.effects()
pg = pltnGpio.pltnGpio()

#distance to activate scheme
actionZone = [10,30]

while True:
    distance = rsDistance.measureAvg()
    print distance 
    
    if actionZone[0] <= distance <= actionZone[-1]:
        ef.ledFlashFade(pg.getPin("g1"), 1, 0.05);