#!/usr/bin/python

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
	"""
	Function: Fade LED strips out from their current values
	Arguments:
		- currentColors: An array of RGB values as follows (r1, r2, b1, b2, g1, g2)
	"""
	# number of steps to go from max to 0 for each color
	STEPS = 20 
	
	#array of iterators 
	iterators = [Decimal(x) / Decimal(STEPS) for x in currentColors]
	
	for i in range(0,STEPS+1):
		print i
		if i == STEPS:
			#set all current values to zero
			for k in range(len(currentColors)):
				currentColors[k] = Decimal(0.00)
			allOff()
			print "exiting loop"
			return
		j = 0
		for j in range(len(currentColors)):
			#decrease each color by its iterator value
			currentColors[j] -= iterators[j]
			#check if the value went negative and set to zero if so
			if currentColors[j] < 0:
				currentColors[j] = Decimal(0)
		#set the new color
		print "still printing even though you exited beyotch"
		setColor(1,[currentColors[0],currentColors[2],currentColors[4]])
		setColor(2,[currentColors[1],currentColors[3],currentColors[5]])
		#turn all the way off if reach the end
		print "currentColors after iteration"
		print currentColors
		#time.sleep(10)
		

#def setColor(ledStripNum,R,G,B):
def setColor(ledStripNum,RGB):
	"""
	Set RGB color passed to it
	LEDstrip: Which strip? (1|2)
	RGB - array of R, G, B values to set
	"""
	#check which strip we want to do stuff to
	if ledStripNum == 1:
		gpioPinsList = GPIO_PINS_LED_1
	elif ledStripNum == 2:
		gpioPinsList = GPIO_PINS_LED_2
	i = 0
	for gpioVal in gpioPinsList:
		os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(gpioVal, Decimal(RGB[i])))
		i += 1

def allOff():
	"""
	Turn all LEDs off
	"""
	setColor(1,[0,0,0])
	setColor(2,[0,0,0])