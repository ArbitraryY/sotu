#!/usr/bin/python

import RPi.GPIO as GPIO
import time as time
 
GPIO.setmode(GPIO.BCM)
 
# Define GPIO to use for PWM
GPIO_PWM =4; 
 
# Set pin as input
GPIO.setup(GPIO_PWM,GPIO.IN) 
 
def measure():
  # Measures a distance (time it takes to go from 0 --> or 1 --> 0)
  
  start = time.time()
  while GPIO.input(GPIO_PWM)==0:
    start = time.time()
  
  while GPIO.input(GPIO_PWM)==1:
    stop = time.time()

  elapsedTime = stop-start
  #distance = (elapsed * 34300)/2 #speed of sound in cm/sec
  distance = (elapsedTime * 13512)/2 #speed of sound in in/sec

  return distance

def measureAvg():
	"""Arguements:
        AVGTYPE - Which average algorithm to use (aMean|median|iquart)
        """
	#avgType = 'aMean'
	avgType = 'median'
        #Number of measurements to take.  Use a multiple of 4 if using the
        #interquartile mean
        numMeasures = 5;
        dataPoints = []
        for num in range(0,numMeasures):
                distance=measure()
                time.sleep(0.05)
                dataPoints.append(distance)
        avg = 0
        if avgType == 'aMean':
                for i in range(0,numMeasures):
                        avg += dataPoints[i]
                        print dataPoints[i]
                avg = avg / numMeasures
        elif avgType == 'median':
		theValues = sorted(dataPoints)
  		if len(theValues) % 2 == 1:
    			avg = theValues[(len(theValues)+1)/2-1]
  		else:
    			lower = theValues[len(theValues)/2-1]
    			upper = theValues[len(theValues)/2]

    			avg = (float(lower + upper)) / 2  
                print "iquart calc"
        elif avgType == 'iquart':
                print "iquart calc"
        else:
                print "not a valid Averaging option"
        return avg


	

'''
  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance
'''
try:
 
  print "Waiting for sensor to settle ..."
 
  # Loop until users quits with CTRL-C
  while True :
 
    # Read and print sensor state
    Current_State = GPIO.input(GPIO_PWM)
    print Current_State 
    #Call distance Avg function
    distance = measureAvg()
    print "Distance : %.1f" % distance
    # time between measurments
    time.sleep(0.5)

except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()
