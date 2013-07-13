#!/usr/bin/python


import sys
sys.path.append("/home/pltn/platoon/Modules")

from pltnGpio import pltnGpio


pg = pltnGpio.pltnGpio()

print pg.getPin('r1')

print pg.getStripPins(2)

print pg.getAllPins()

print pg.getPinBothStrips('r')
print pg.getPinBothStrips('g')
print pg.getPinBothStrips('b')