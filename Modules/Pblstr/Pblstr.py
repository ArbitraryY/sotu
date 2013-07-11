#!/usr/bin/python

from os import system

class Pblstr:
    def __init__(self):
        #specify the Pi-Blaster device file
        self.devFile = '/dev/pi-blaster'
    
    def write(self,gpioPin,currentVal):
        """
        This function writes to the pi-blaster device file
            INPUT: 
                - gpioPin = A GPIO pin
                - currentVal = the value to set the pin to
        """
        system("echo \"{0}={1}\" > {2}" .format(gpioPin,currentVal,self.devFile))