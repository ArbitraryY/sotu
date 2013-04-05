#!/usr/bin/python

import pyfirmata
import time

#setup serial connection to Arduino
board = pyfirmata.Arduino('/dev/ttyACM0')

# start an iterator thread so that serial buffer doesn't overflow
it = pyfirmata.util.Iterator(board)
it.start()

#set the number of measurements to take and the type of Mean. 
#Options are aMean (arithmetic Mean), median, iquart (interquartile average)

global avgType
avgType = 'median'
global numMeasures
numMeasures = 10

# set up pins
pin0=board.get_pin('a:0:i')             # A0 Input      (LM35)

def arduinoMeasure():
	'''
	This function measures the distance when the range sensor is connected to pin A0 
	on the Arduino
	'''
	#print pin0.read()
	while pin0.read() is None:
        	print "passing"
        	pass
	#distance = (pin0.read()*1024)/2
	distance = (pin0.read()*1023)/2
	#print "distance: %.f" % distance
	#board.pass_time(3)
        return distance

def piMeasure(GPIO_RS):
        """This function measures the distance the echo pulse has traveled.
        i.e. the time it takes for the sensor to go from 0 --> 1 or 1 --> 0)
	GPIO_RS
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
        """Arguements:
        AVGTYPE - Which average algorithm to use (aMean|median|iquart)
        """
        #Number of measurements to take.  Use a multiple of 4 if using the
        #interquartile mean
        dataPoints = []
        #take numMeasures # of measurements and put into array for avg calculations
        for num in range(0,numMeasures):
                distance=arduinoMeasure()
                time.sleep(0.01)
                dataPoints.append(distance)
        avg = 0
        #calculate the Arithmetic Mean
        if avgType == 'aMean':
                for i in range(0,numMeasures):
                        avg += dataPoints[i]
                        print avg
                avg = avg / numMeasures
        #calculate the Median
        elif avgType == 'median':
                #calculate the median
                theValues = sorted(dataPoints)
                if len(theValues) % 2 == 1:
                        print int((len(theValues)+1)/2-1)
                        avg = theValues[int((len(theValues)+1)/2-1)]
                else:
                        lower = theValues[int(len(theValues)/2-1)]
                        upper = theValues[int(len(theValues)/2)]
                        avg = (float(lower + upper)) / 2
        elif avgType == 'iquart':
                print "iquart calc"
        else:
                print "not a valid Averaging option"
        return avg

