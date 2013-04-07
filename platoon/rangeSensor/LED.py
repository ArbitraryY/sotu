#!/usr/bin/python

#from __future__ import division
from decimal import *
import os
import time
import rsDistance

#set Decimal precision to 2 places
getcontext().prec = 2

GPIO_PINS_LED_1 = [2,5,7]
GPIO_PINS_LED_2 = [1,4,6]

def analogToDigital(analogColors):
	'''
	Accepts a 2D list of analog RGB values (analogColors) and converts them 	to digital.
	Returns - 2D list of digital RGB values (digitalColors)
	'''
	digitalColors = [[Decimal(x)/Decimal(255) for x in y] for y in analogColors]
	return digitalColors

def fadeLED( gpio, startVal, stopVal, lower, upper, STEP, FADESPEED):
    """This function takes the following arguments
    gpio: value of the RPi GPIO pin that will be updated
    startVal: RGB value that the fade will start from
    stopVal: RGB value that the fade will stop at
    lower: Lower bound of the current range
    upper: Upper bound of the current range
    STEP: step size between LED transitions
    FADESPEED: decrease to slow fading must be 2 digit Decimal data type
        
    If the stop value is higher need to increment to get there.
    If the stop value is lower need to decrement to get there
    
    Returns rangeVal: (0|1) if user is out/in range
    currentVal: Returns the value of the current RGB setting
    This is needed to fade out from whatever state the LEDs are currently at  
    """
	#this variable will be returned as a check whether or not someone is in/out
	#of range
    rangeVal = 1;
    #set the current LED values to the start value
    currentVal = startVal
    if startVal < stopVal:
        while currentVal < stopVal:
            os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(gpio,currentVal))
            currentVal = currentVal + STEP;
            time.sleep(FADESPEED)
            #take a distance measurement and check if out of range
            distance = rsDistance.measureAvg()
            if distance < lower or distance > upper:
                rangeVal = 0;
                #if user exits range return the current value to populate
                #the currentColors array.  Need this for proper fade out
                return rangeVal, currentVal
    elif startVal > stopVal:
        while currentVal > stopVal:
            os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(gpio,currentVal))
            currentVal = currentVal - STEP;
            time.sleep(FADESPEED)
            #take a distance measurement
            distance = rsDistance.measureAvg()
            #print "distance in loop subtracting loop: %.3f" % distance
            if distance < lower or distance > upper:
                rangeVal = 0;
                return rangeVal, currentVal
    
    return rangeVal, currentVal;

def fadeOutLED(currentColors):	
	print "Fading out here"
	print currentColors
#	i = 1/255
	i = 0
	if currentColors[0] > i:
		currentColors[0] -= i
	if currentColors[1] > i:
		currentColors[1] -= i
	if currentColors[2] > i:
		currentColors[2] -= i
	if currentColors[3] > i:
		currentColors[3] -= i
	if currentColors[4] > i:
		currentColors[4] -= i
	if currentColors[5] > i:
		currentColors[5] -= i
		
	setColor(1,currentColors[0],currentColors[2],currentColors[4])
	setColor(2,currentColors[1],currentColors[3],currentColors[5])
	print currentColors
	time.sleep(10)

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
		os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(gpioVal, Decimal(RGB[i])))
		#print gpioVal, Decimal(RGB[i])
		i += 1

def allOff():
	"""
	Turn all LEDs off
	"""
	setColor(1,0,0,0)
	setColor(2,0,0,0)