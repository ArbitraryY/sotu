#!/usr/bin/python
"""@package rangeSensor
Documentation for this module

"""
from __future__ import division
import RPi.GPIO as GPIO
import time as time
from subprocess import call
import time
import os

# Define GPIO to use for range Sensor
GPIO_RS =4; 
#define the GPIO pins, r = 5, g = 2, b = 6
GPIO_PINS_LED_1 = [2,5,7]
GPIO_PINS_LED_2 = [1,4,6]

#set mode to BCM so PWM
GPIO.setmode(GPIO.BCM)
 
# Set pin as input
GPIO.setup(GPIO_RS,GPIO.IN) 
 
#define global step size for fading theough colors
global FADESPEED
global STEP

FADESPEED = 0.01 #Increase to slow down
STEP = 0.03

# define LED RGB colors
RNG_1_LED_1 = [ [28,30,68],[40,93,144],[255,255,255],[40,93,144],[123,32,144],[67,47,103] ]
RNG_1_LED_2 = [ [150,44,37],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]

#RNG_2_LED_1 = [ [0,0,0],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]
#RNG_2_LED_2 = [ [150,44,37],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]

#RNG_3_LED_1 = [ [150,44,37],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]
#RNG_3_LED_2 = [ [150,44,37],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]

#define ranges
ranges=[10.0,16.0,17.0,47.0,48.0,70.0];

#----------------------Funcs-----------------------------------------
def measure():
	"""This function measures the distance the echo pulse has traveled.
	i.e. the time it takes for the sensor to go from 0 --> 1 or 1 --> 0)
	"""
 	start = time.time()
  	while GPIO.input(GPIO_RS)==0:
    		start = time.time()
	while GPIO.input(GPIO_RS)==1:
    		stop = time.time()
	elapsedTime = stop-start
  	#distance = (elapsed * 34300)/2 #speed of sound in cm/sec
  	distance = (elapsedTime * 13512)/2 #speed of sound in in/sec
	return distance

def measureAvg():
	"""Take 3 measurements and returns the average
	"""
	distance1=measure()
  	time.sleep(0.15)
  	distance2=measure()
  	time.sleep(0.15)
  	distance3=measure()
  	time.sleep(0.15)
  	distance4=measure()
  	time.sleep(0.15)
  	distance5=measure()
  	time.sleep(0.15)
  	distance6=measure()
  	time.sleep(0.15)
  	distance7=measure()
  	time.sleep(0.15)
  	distance = distance1 + distance2 + distance3 + distance4 + distance5 + distance6 + distance7
  	distance = distance / 7
  	return distance

def fadeLED( gpio, startVal, stopVal, lower, upper ):
        """This function takes the following arguements
        gpio: value of the RPi GPIO pin that will be updated
        startVal: RGB value that the fade will start from
        stopVal: RGB value that the fade will stop at
	lower: Lower bound of the current range
	upper: Upper bound of the current range 

        If the stop value is higher need to increment to get there.
        If the stop value is lower need to decrement to get there
        """
        #convert passed values into usable format for pi-blaster (i.e 0 - 1)
        RGBstartVal = startVal / 255
        RGBstopVal = stopVal / 255
        #debug
        #print RGBstartVal, startVal, RGBstopVal, stopVal;
        #set the current LED values to the start value
	
        currentVal = RGBstartVal
        if RGBstartVal < RGBstopVal:
                while currentVal < RGBstopVal:
                        os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(gpio,currentVal))
                        currentVal = currentVal + STEP;
                        time.sleep(FADESPEED)
    			#take a distance measurment and check if out of range
			distance = measure()
			print "distance in loop addition loop: %.3f" % distance
			if distance < lower or distance > upper:
				allOff();
				break
                        #print currentVal
        elif RGBstartVal > RGBstopVal:
                 while currentVal > RGBstopVal:
                        os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(gpio,currentVal))
                        currentVal = currentVal - STEP;
                        time.sleep(FADESPEED)
    			#take a distance measurment
			distance = measure()
			print "distance in loop subtracting loop: %.3f" % distance
			if distance < lower or distance > upper:
				allOff();
				break
                        #print currentVal
        return;

def allOff():
	"""This function turns all the LEDs off
	"""
	for gpioVal in GPIO_PINS_LED_1:
        	os.system("echo \"{0}=0\" > /dev/pi-blaster" .format(gpioVal))
	for gpioVal in GPIO_PINS_LED_2:
        	os.system("echo \"{0}=0\" > /dev/pi-blaster" .format(gpioVal))
	
	

#-------------------End Funcs -----------------------------------------

try:
 
  print "Waiting for sensor to settle ..."
 
  # Loop until users quits with CTRL-C
  while True : 
    	# Read and print sensor state
    	Current_State = GPIO.input(GPIO_RS)
    	print Current_State 
    	#take a distance measurment
	distance = measure()
    	print "Distance : %.1f" % distance
	#check which range we are in
	#if distance >= ranges[0] and distance <= ranges[1]:
	i = 0
	j = 0
	while distance >= ranges[0] and distance <= ranges[1]:
		print "------------Range 1-----------"
		#set LED to initial value
		
		#determine the number of colors in each array	
		LED_1_COLORS_LENGTH = len(RNG_1_LED_1)
		LED_2_COLORS_LENGTH = len(RNG_1_LED_2)
		#measure distance again and exit loop if out of range
		distance = measure()
		print "distance in loop: %.3f" % distance
		if distance < ranges[0] or distance > ranges[1]:
			allOff()
			break	
		#fade red LEDs
		fadeLED(GPIO_PINS_LED_1[0],RNG_1_LED_1[i][0],RNG_1_LED_1[i+1][0],ranges[0],ranges[1]);
		fadeLED(GPIO_PINS_LED_2[0],RNG_1_LED_2[j][0],RNG_1_LED_2[j+1][0],ranges[0],ranges[1]);	
		#fade green LEDs
		fadeLED(GPIO_PINS_LED_1[1],RNG_1_LED_1[i][1],RNG_1_LED_1[i+1][1],ranges[0],ranges[1]);
		fadeLED(GPIO_PINS_LED_2[1],RNG_1_LED_2[j][1],RNG_1_LED_2[j+1][1],ranges[0],ranges[1]);	
		#fade blue LEDs
		fadeLED(GPIO_PINS_LED_1[2],RNG_1_LED_1[i][2],RNG_1_LED_1[i+1][2],ranges[0],ranges[1]);
		fadeLED(GPIO_PINS_LED_2[2],RNG_1_LED_2[j][2],RNG_1_LED_2[j+1][2],ranges[0],ranges[1]);	
		i = i + 1
		j = j + 1
		#check if array dimensions have gone out of range
		if i > LED_1_COLORS_LENGTH - 2:
			i = 0
		if j > LED_2_COLORS_LENGTH - 2:
			j = 0
		print i , j
		print LED_1_COLORS_LENGTH, LED_2_COLORS_LENGTH
		'''
		for c in range(len(RNG_1_LED_1)-1):
        		#loop within each subarray
        		for a in range(len(RNG_1_LED_1[c])):
                		#pass GPIO pin to which manipulate
               			fadeLED(GPIO_PINS_LED_1[a],RNG_1_LED_1[c][a],RNG_1_LED_1[c+1][a]);
	
        	print "--------------------"
		'''

	'''
	elif distance >= ranges[2] and distance <= ranges[3]:
		print "------------Range 2-----------"
	elif distance >= ranges[4] and distance <= ranges[5]:
		print "------------Range 3-----------"
	else
		print "not in range"
	'''

    # time between measurments
    	time.sleep(1)

except KeyboardInterrupt:
	for gpioVal in GPIO_PINS_LED_1:
        	os.system("echo \"{0}=0\" > /dev/pi-blaster" .format(gpioVal))
	for gpioVal in GPIO_PINS_LED_2:
        	os.system("echo \"{0}=0\" > /dev/pi-blaster" .format(gpioVal))

		print "  Quit"
  	# Reset GPIO settings
  	GPIO.cleanup()
