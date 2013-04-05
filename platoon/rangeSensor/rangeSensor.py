#!/usr/bin/python
"""@package rangeSensor
Documentation for this module

"""
from __future__ import division #needed for division of integers --> floats
import RPi.GPIO as GPIO
import time
import os
import rsDistance
import LED

# Define GPIO to use for range Sensor
#GPIO_RS =4; 
#define the GPIO pins for each strip
GPIO_PINS_LED_1 = [2,5,7]
GPIO_PINS_LED_2 = [1,4,6]

#set mode to BCM so PWM
GPIO.setmode(GPIO.BCM)
 
# Set range sensor pin as an input. Need thisin order to overtake the setting
# from pi-blaster which sets all GPIO pins to input
#GPIO.setup(GPIO_RS,GPIO.IN) 
 
#define global step size for fading theough colors
global FADESPEED
global STEP

#Increase to slow down LED color changes
FADESPEED = 0.01
#step size to jump to the next RGB value when fading.  Increasing this will
#will slow down the fade
STEP = 0.02

# define Analog LED RGB colors
RNG_1_LED_1_ANALOG = [ [28,30,68],[40,93,144],[255,255,255],[40,93,144],[123,32,144],[67,47,103] ]
RNG_1_LED_2_ANALOG = [ [150,44,37],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]
#RNG_2_LED_1_ANALOG = [ [0,0,0],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]
#RNG_2_LED_2_ANALOG = [ [150,44,37],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]
#RNG_3_LED_1_ANALOG = [ [150,44,37],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]
#RNG_3_LED_2_ANALOG = [ [150,44,37],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]

#Convert Analog RGB values to Digital
RNG_1_LED_1 = LED.analogToDigital(RNG_1_LED_1_ANALOG)
RNG_1_LED_2 = LED.analogToDigital(RNG_1_LED_2_ANALOG)
#RNG_2_LED_1 = analogToDigital(RNG_1_LED_2_ANALOG)
#RNG_2_LED_2 = analogToDigital(RNG_1_LED_2_ANALOG)
#RNG_3_LED_1 = analogToDigital(RNG_1_LED_2_ANALOG)
#RNG_3_LED_2 = analogToDigital(RNG_1_LED_2_ANALOG)

#define ranges
ranges=[10.0,16.0,17.0,47.0,48.0,70.0];

#----------------------Funcs-----------------------------------------
def fadeLED( gpio, startVal, stopVal, lower, upper ):
        """This function takes the following arguments
        gpio: value of the RPi GPIO pin that will be updated
        startVal: RGB value that the fade will start from
        stopVal: RGB value that the fade will stop at
	    lower: Lower bound of the current range
	    upper: Upper bound of the current range 

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
    			#take a distance measurment and check if out of range
			distance = rsDistance.measureAvg()
			#print "distance in loop addition loop: %.3f" % distance
			if distance < lower or distance > upper:
				LED.allOff();
				rangeVal = 0;
				break
                        print currentVal
        elif startVal > stopVal:
                 while currentVal > stopVal:
                        os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(gpio,currentVal))
                        currentVal = currentVal - STEP;
                        time.sleep(FADESPEED)
    			#take a distance measurment
			distance = rsDistance.measureAvg()
			#print "distance in loop subtracting loop: %.3f" % distance
			if distance < lower or distance > upper:
				LED.allOff();
				rangeVal = 0;
				break
			print currentVal
        return rangeVal, currentVal;
'''
def #fadeOutLED(currentColors):	
	print "Fading out here"
	print currentColors
	i = 1/255
	if currentColors[0] > i:
		currentColors[0] =- i
	if currentColors[1] > i:
		currentColors[1] =- i
	if currentColors[2] > i:
		currentColors[2] =- i
	if currentColors[3] > i:
		currentColors[3] =- i
	if currentColors[4] > i:
		currentColors[4] =- i
	if currentColors[5] > i:
		currentColors[5] =- i
		
	setColor(1,currentColors[0],currentColors[2],currentColors[4])
	setColor(2,currentColors[1],currentColors[3],currentColors[5])
	print currentColors
	time.sleep(10)
'''

#-------------------End Funcs -----------------------------------------

try:
 
  print "Waiting for sensor to settle ..."
 
  # Loop until users quits with CTRL-C
  while True : 
	i = 0
	j = i + 1
	k = 0
	m = k + 1
    	#take a distance measurment
	distance = rsDistance.measureAvg()
    	print "Average Distance : %.1f" % distance
	#check which range we are in
	#set initial LED colors fadeIn function will replace this when written
	if distance >= ranges[0] and distance <= ranges[1]:
		#setColor(GPIO_PINS_LED_1[0],RNG_1_LED_1[i][0])
		LED.setColor(1,RNG_1_LED_1[0][0],RNG_1_LED_1[0][1],RNG_1_LED_1[0][2])
		LED.setColor(2,RNG_1_LED_2[0][0],RNG_1_LED_2[0][1],RNG_1_LED_2[0][2])
		#Holds all currently set colors.  This will be passed to fadeIn/Out functions
		currentColors = [RNG_1_LED_1[0][0],RNG_1_LED_2[0][0],RNG_1_LED_1[0][1],RNG_1_LED_2[0][1],RNG_1_LED_1[0][2],RNG_1_LED_2[0][2]]
		print 'In initial Color Define range'
		#fadeInLed(currentColors)
	#elif distance >= ranges[2] and distance <= ranges[3]:
	#elif distance >= ranges[4] and distance <= ranges[5]:
	
	rangeVal = 1;	
	while distance >= ranges[0] and distance <= ranges[1]:
		print "------------Range 1-----------"
		#determine the number of colors in each array	
		LED_1_COLORS_LENGTH = len(RNG_1_LED_1)
		LED_2_COLORS_LENGTH = len(RNG_1_LED_2)
		#measure distance again and exit loop if out of range
		distance = rsDistance.measureAvg()
		print "distance in loop: %.3f" % distance
		if distance < ranges[0] or distance > ranges[1]:
			LED.allOff()
			##fadeOutLED(currentColors)
			break	
		#fade red LEDs
		if(rangeVal):
			#rangeVal, currentColors[0] = fadeLED(GPIO_PINS_LED_1[0],RNG_1_LED_1[i][0],RNG_1_LED_1[i+1][0],ranges[0],ranges[1])
			rangeVal, currentColors[0] = fadeLED(GPIO_PINS_LED_1[0],RNG_1_LED_1[i][0],RNG_1_LED_1[j][0],ranges[0],ranges[1])
		#else:
			##fadeOutLED(currentRedVal1, currentRedVal2, currentBlueVal1, currentBlueVal2, currentGreenVal1, currentGreenVal2)
			#fadeOutLED(currentColors)
		if(rangeVal):
			#rangeVal, currentColors[1] = fadeLED(GPIO_PINS_LED_2[0],RNG_1_LED_2[j][0],RNG_1_LED_2[j+1][0],ranges[0],ranges[1])
			rangeVal, currentColors[1] = fadeLED(GPIO_PINS_LED_2[0],RNG_1_LED_2[k][0],RNG_1_LED_2[m][0],ranges[0],ranges[1])
		#else:
			##fadeOutLED(currentRedVal1, currentRedVal2, currentBlueVal1, currentBlueVal2, currentGreenVal1, currentGreenVal2)
			#fadeOutLED(currentColors)
		#fade green LEDs
		if(rangeVal):
			#rangeVal, currentColors[2] = fadeLED(GPIO_PINS_LED_1[1],RNG_1_LED_1[i][1],RNG_1_LED_1[i+1][1],ranges[0],ranges[1])
			rangeVal, currentColors[2] = fadeLED(GPIO_PINS_LED_1[1],RNG_1_LED_1[i][1],RNG_1_LED_1[j][1],ranges[0],ranges[1])
		#else:
			##fadeOutLED(currentRedVal1, currentRedVal2, currentBlueVal1, currentBlueVal2, currentGreenVal1, currentGreenVal2)
			#fadeOutLED(currentColors)
		if(rangeVal):
			#rangeVal, currentColors[3] = fadeLED(GPIO_PINS_LED_2[1],RNG_1_LED_2[j][1],RNG_1_LED_2[j+1][1],ranges[0],ranges[1])	
			rangeVal, currentColors[3] = fadeLED(GPIO_PINS_LED_2[1],RNG_1_LED_2[k][1],RNG_1_LED_2[m][1],ranges[0],ranges[1])	
		#else:
			##fadeOutLED(currentRedVal1, currentRedVal2, currentBlueVal1, currentBlueVal2, currentGreenVal1, currentGreenVal2)
			#fadeOutLED(currentColors)
		#fade blue LEDs
		if(rangeVal):
			#rangeVal, currentColors[4] = fadeLED(GPIO_PINS_LED_1[2],RNG_1_LED_1[i][2],RNG_1_LED_1[i+1][2],ranges[0],ranges[1])
			rangeVal, currentColors[4] = fadeLED(GPIO_PINS_LED_1[2],RNG_1_LED_1[i][2],RNG_1_LED_1[j][2],ranges[0],ranges[1])
		#else:
			##fadeOutLED(currentRedVal1, currentRedVal2, currentBlueVal1, currentBlueVal2, currentGreenVal1, currentGreenVal2)
			#fadeOutLED(currentColors)
		if(rangeVal):
			#rangeVal, currentColors[5] = fadeLED(GPIO_PINS_LED_2[2],RNG_1_LED_2[j][2],RNG_1_LED_2[j+1][2],ranges[0],ranges[1])	
			rangeVal, currentColors[5] = fadeLED(GPIO_PINS_LED_2[2],RNG_1_LED_2[k][2],RNG_1_LED_2[m][2],ranges[0],ranges[1])	
		#else:
			##fadeOutLED(currentRedVal1, currentRedVal2, currentBlueVal1, currentBlueVal2, currentGreenVal1, currentGreenVal2)
			#fadeOutLED(currentColors)
		
		#print 'before'
		#print i, j, k, m
		#time.sleep(5)
		#Color rotation logic
		if i < (LED_1_COLORS_LENGTH - 1):
			i = i + 1
		elif i == (LED_1_COLORS_LENGTH - 1):
			i = 0
		if j < (LED_1_COLORS_LENGTH - 1):
			j = j + 1
		elif j == (LED_1_COLORS_LENGTH - 1):
			j = 0
		if k < (LED_2_COLORS_LENGTH - 1):
			k = k + 1
		elif k == (LED_2_COLORS_LENGTH - 1):
			k = 0
		if m < (LED_2_COLORS_LENGTH - 1):
			m = m + 1
		elif m == (LED_2_COLORS_LENGTH - 1):
			m = 0
		
		#print 'after'
		#print i, j, k, m
		#time.sleep(5)
		#print LED_1_COLORS_LENGTH, LED_2_COLORS_LENGTH
		#print currentRedVal1, currentRedVal2, currentBlueVal1, currentBlueVal2, currentGreenVal1, currentGreenVal2
		#time.sleep(5)
		print 'At end of one fade'
		#print currentColors
		#time.sleep(3)

	'''
	elif distance >= ranges[2] and distance <= ranges[3]:
		print "------------Range 2-----------"
	elif distance >= ranges[4] and distance <= ranges[5]:
		print "------------Range 3-----------"
	else
		print "not in range"
	'''

    # time between measurments
    	time.sleep(0.01)

except KeyboardInterrupt:
	LED.allOff()
	print "  Quit"
  	# Reset GPIO settings
  	GPIO.cleanup()
