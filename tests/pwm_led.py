#!/usr/bin/python

"""@package rangeSensor
Documentation for this module

"""

from __future__ import division
from subprocess import call
import time
import os

#define the GPIO pins, r = 5, g = 2, b = 6
GPIO_PINS_LED_1 = [5,2,6]
#GPIO_PINS_LED_2 = [5,2,6]

#define global step size for fading theough colors
global FADESPEED
global STEP

FADESPEED = 0.1 #Increase to slow down
STEP = 0.03

RNG_1_LED_1 = [ [28,30,68],[40,93,144],[255,255,255],[40,93,144],[123,32,144],[67,47,103] ]
RNG_1_LED_2 = [ [150,44,37],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]



#-----------Funcs
def fadeLED( gpio, startVal, stopVal ):
	"""This function takes 3 values
	gpio - value of the RPi GPIO pin that will be updated
	startVal - RGB value that the fade will start from
	stopVal - RGB value that the fade will stop at	
	
	If the stop value is higher need to increment to get there.
	If the stop value is lower need to decrement to get there
	"""
	#convert passed values into usable format for pi-blaster (i.e 0 - 1)
	RGBstartVal = startVal / 255
	RGBstopVal = stopVal / 255
	#debug
	print RGBstartVal, startVal, RGBstopVal, stopVal;
	#set the current LED values to the start value
	currentVal = RGBstartVal
	if RGBstartVal < RGBstopVal:
		while currentVal < RGBstopVal:
			os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(gpio,currentVal))
			currentVal = currentVal + STEP;
			time.sleep(FADESPEED)
			print currentVal
	elif RGBstartVal > RGBstopVal:
		 while currentVal > RGBstopVal:
			os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(gpio,currentVal))
                        currentVal = currentVal - STEP;
                        time.sleep(FADESPEED)
                        print currentVal
	return;

#-----------END of Fucns

#take a range measurement here dont forget to set initial pin values to 
#first color in array


#loop through main arrays
#c indicates which color, a indicates which array are we are in
for c in range(len(RNG_1_LED_1)-1):
	#loop within each subarray
	for a in range(len(RNG_1_LED_1[c])):
		#pass GPIO pin to which manipulate
		fadeLED(GPIO_PINS_LED_1[a],RNG_1_LED_1[c][a],RNG_1_LED_1[c+1][a]);
	print "--------------------"
	#time.sleep(1)
#turn off when done
for gpioVal in GPIO_PINS_LED_1:
	os.system("echo \"{0}=0\" > /dev/pi-blaster" .format(gpioVal))
	
