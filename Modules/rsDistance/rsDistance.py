#!/usr/bin/python
"""@package rsDistance

	This module calculates range sensor measurements.  It uses an echo pulse
	algorithm to calculate the range from the voltage readings of the range sensor
	connected to the Arduino.  It uses pyfirmata to communicate with the Arduino over 
	serial USB.  
"""

import pyfirmata
import time
import numpy as np

#setup serial connection to Arduino
board = pyfirmata.Arduino('/dev/ttyACM0')

# start an iterator thread so that serial buffer doesn't overflow
it = pyfirmata.util.Iterator(board)
it.start()

#set the number of measurements to take and the type of Mean. 
#Options are aMean (arithmetic Mean), median
global avgType
avgType = 'median'
#the number of measurements to take for averaging
global numMeasures
numMeasures = 10

# Set up the RPi to read the analog values from pin 0 on the Arduino
pin0=board.get_pin('a:0:i') 

def arduinoMeasure():
	"""(RS connected to Arduino) This function measures the distance of the nearest object
		in the range of the range sensor
		Input: None
		Return:
			distance: The distance in inches an object is from the range sensor
	"""
	while pin0.read() is None:
        	print "passing"
        	pass
	distance = (pin0.read()*1023)/2
        return distance

def piMeasure(GPIO_RS):
        """(RS connected to RPi) this function will measure the distance the echo pulse has 
        	traveled. i.e. the time it takes for the sensor to go from 0 --> 1 or 1 --> 0) 
        	Input: 
           		GPIO_RS: The GPIO pin that the range sensor is connected to 
       		Return: 
           		distance: The distance an object is from the range sensor
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
		"""This function takes "numMeasures" number of range sensor measurements and smoothes them 
			out using averaging function (AVGTYPE) using either Arithmetic Mean (aMean) or median.
        	Input: None
        	Return:
				avg: The average value of "numMeasures" range sensor measurements		
        """
		#Number of measurements to take
		dataPoints = []
		#take numMeasures # of measurements and put into array for avg calculations
		for num in range(0,numMeasures):
        	#measure the range numMeasures times and put them into an array
			distance=arduinoMeasure()
			time.sleep(0.01)
			dataPoints.append(distance)
		avg = 0
		#calculate the Arithmetic Mean
		if avgType == 'aMean':
			avg = np.mean(dataPoints)
		#calculate the Median
		elif avgType == 'median':
			avg = np.median(dataPoints)
		else:
			print "not a valid Averaging option"
		return avg

