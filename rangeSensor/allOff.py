#!/usr/bin/python

import os

ALL_GPIO_PINS   = [2,1,5,4,7,6]

"""
set all GPIO to off
"""
for pin in ALL_GPIO_PINS:
    os.system("echo \"{0}=0\" > /dev/pi-blaster" .format(pin))