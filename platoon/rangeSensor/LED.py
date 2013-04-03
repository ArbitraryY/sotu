#!/usr/bin/python

from __future__ import division
import os

GPIO_PINS_LED_1 = [2,5,7]
GPIO_PINS_LED_2 = [1,4,6]

def analogToDigital(analogColors):
	'''
	Accepts a 2D list of analog RGB values (analogColors) and converts them 	to digital.
	Returns - 2D list of digital RGB values (digitalColors)
	'''
        digitalColors = [[x/255 for x in y] for y in analogColors]
        return digitalColors

def setColor(ledStripNum,R,G,B):
        """
        Set RGB color passed to it
        LEDstrip: Which strip? (1|2)
        R,G,B - color values to set
        """
        #Put RGB values into an array
        RGB = [R,G,B]
        #check which strip we want to do stuff to
        if ledStripNum == 1:
                gpioPinsList = GPIO_PINS_LED_1
        elif ledStripNum == 2:
                gpioPinsList = GPIO_PINS_LED_2
        i = 0
        for gpioVal in gpioPinsList:
                os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(gpioVal, RGB[i]))
                print gpioVal, RGB[i]
                i += 1

def allOff():
        """
        Turn all LEDs off
        """
        setColor(1,0,0,0)
        setColor(2,0,0,0)

