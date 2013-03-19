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
GPIO_RS =22; 
#define the GPIO pins, r = 5, g = 2, b = 6
GPIO_PINS_LED_1 = [5,2,6]
#GPIO_PINS_LED_2 = [5,2,6]

#set mode to BCM so PWM
GPIO.setmode(GPIO.BCM)
 
# Set pin as input
GPIO.setup(GPIO_RS,GPIO.IN) 
 
#define global step size for fading theough colors
global FADESPEED
global STEP

FADESPEED = 0.1 #Increase to slow down
STEP = 0.03

# define LED RGB colors
RNG_1_LED_1 = [ [28,30,68],[40,93,144],[255,255,255],[40,93,144],[123,32,144],[67,47,103] ]
RNG_1_LED_2 = [ [150,44,37],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]

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
  	time.sleep(0.1)
  	distance2=measure()
  	time.sleep(0.1)
  	distance3=measure()
  	distance = distance1 + distance2 + distance3
  	distance = distance / 3
  	return distance

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
	if distance >= ranges[0] and distance <= ranges[1]:
		print "in range 1 yo"
	elif distance >= ranges[2] and distance <= ranges[3]:
		print "in range 2 yo"
	elif distance >= ranges[4] and distance <= ranges[5]:
		print "in range 3 yo"
	else:
		print "not in range"


    # time between measurments
    	time.sleep(1)

except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()
