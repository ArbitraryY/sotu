#!/usr/bin/python

import os
import Pblstr as Pblstr

ALL_GPIO_PINS   = [2,1,5,4,7,6]

pb = Pblstr.Pblstr()

"""
set all GPIO to off
"""
for pin in ALL_GPIO_PINS:
    pb.write(pin,0)