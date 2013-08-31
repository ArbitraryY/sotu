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
#for pin in ALL_GPIO_PINS:
pb.write(2,0)
pb.write(5,0)
pb.write(7,1)
pb.write(1,0)
pb.write(4,0)
pb.write(6,1)
