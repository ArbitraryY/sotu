#!/usr/bin/python

import sys
sys.path.append("/usr/local/pltn/Modules")
from Pblstr import Pblstr
from pltnGpio import pltnGpio

#instantiate objects
pg = pltnGpio.pltnGpio()
pb = Pblstr.Pblstr()

ALL_GPIO_PINS = pg.getAllPins('asList')

"""
set all GPIO to off
"""
for pin in ALL_GPIO_PINS:
    pb.write(pin,0)