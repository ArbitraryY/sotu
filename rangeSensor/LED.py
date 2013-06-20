#!/usr/bin/python

from decimal import *
import os
import time
import rsDistance
import threading
import Pblstr
#set Decimal precision to 2 places
getcontext().prec = 2

GPIO_PINS_LED_1 = [2,5,7]
GPIO_PINS_LED_2 = [1,4,6]
ALL_GPIO_PINS   = [2,1,5,4,7,6]

#create pblstr object. Use this for all writes to pi-Blaster device file
pb = Pblstr.Pblstr()

def analogToDigital(analogColors):
	'''
	Accepts a 2D list of analog RGB values (analogColors) and converts them 	to digital.
	Returns - 2D list of digital RGB values (digitalColors)
	'''
	digitalColors = [[Decimal(x)/Decimal(255) for x in y] for y in analogColors]
	return digitalColors

def fadeLED( gpio, startVal, stopVal, lower, upper, STEP, FADESPEED ):
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
    rangeVal = 1
    #set the current LED values to the start value
    currentVal = startVal
    if startVal < stopVal:
        while currentVal < stopVal:
            os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(gpio,currentVal))
            currentVal += STEP;
            time.sleep(FADESPEED)
            print "GPIO: {0}, Value = {1}" .format(gpio,currentVal)
            #take a distance measurement and check if out of range
            distance = rsDistance.measureAvg()
            #print "\n\n this is the distance n fade loop: %f \n\n" % distance
            if distance < lower:
            	rangeVal = 0
            	return rangeVal, currentVal
            elif distance > upper:
            	#print "this is the distance while in the subtracting fade loop: %f" % distance
            	#time.sleep(5)
            	rangeVal = 2
            	return rangeVal, currentVal
            else:
				rangeVal = 1
				"""
			if distance < lower or distance > upper:
				#if user exits range return the current value to populate
				#the currentColors array.  Need this for proper fade out
				rangeVal = 0
				return rangeVal, currentVal
            else:
            	rangeVal = 1
			"""    
    elif startVal > stopVal:
        while currentVal > stopVal:
            os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(gpio,currentVal))
            currentVal -= STEP;
            time.sleep(FADESPEED)
            print "GPIO: {0}, Value = {1}" .format(gpio,currentVal)
            #take a distance measurement
            distance = rsDistance.measureAvg()
            #print "\n\n this is the distance n fade loop: %f \n\n" % distance
            #time.sleep(10)
            #print "distance in loop subtracting loop: %.3f" % distance
#            if distance < lower or distance > upper:
            if distance < lower:
                rangeVal = 0
                return rangeVal, currentVal
            elif distance > upper:
            	#print "this is the distance while in the subtracting fade loop: %f" % distance
            	#time.sleep(5)
                rangeVal = 2
                return rangeVal, currentVal
            else:
            	rangeVal = 1
    
    return rangeVal, currentVal;

def fadeOutLED2(currentColors,distance):
	print "distance when entering fade out loop: %f" % distance
	#time.sleep(10) 
	STEP = Decimal(0.01)
	FADESPEED = Decimal(0.01)
	for i in range(len(currentColors)):
		#fadeLED(ALL_GPIO_PINS[i],currentColors[i],Decimal(0.00),0,200,Decimal(0.01),Decimal(0.00))
		while currentColors[i] > Decimal(0.00):
			os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(ALL_GPIO_PINS[i],currentColors[i]))
			currentColors[i] -= Decimal(STEP);
			#set to zero once it gets negative
			if currentColors[i] < Decimal(0):
				os.system("echo \"{0}=0\" > /dev/pi-blaster" .format(ALL_GPIO_PINS[i]))
				#set current colors to zero before exiting loop
				currentColors[i] = 0
			#time.sleep(FADESPEED)
			print "in fade out loop: %f" % currentColors[i]
	currentColors[i]=0
	allOff()
	
def fadeOutLED3(gpioPinVal, currentVal, stepSize):
	'''
	This function takes a GPIO pin value and a current LED color
	value and fades it to 0
	'''
	print "hello from thread: %i" % gpioPinVal
	print "fading out now"
	STEP = Decimal(stepSize)
	FADESPEED = Decimal(0.01)
	while currentVal > Decimal(0.00):
		os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(gpioPinVal,currentVal))
		currentVal -= Decimal(STEP);
		#set to zero once it gets negative
		if currentVal < Decimal(0):
			os.system("echo \"{0}=0\" > /dev/pi-blaster" .format(gpioPinVal))
			#set current colors to zero before exiting loop
			currentVal = 0
		#time.sleep(FADESPEED)
		print "%0.2f" % currentVal
	
def fadeOutLED(currentColors,numSteps):
	"""
	Function: Fade LED strips out from their current values
	Arguments:
		- currentColors: An array of RGB values as follows (r1, r2, b1, b2, g1, g2)
		- numSteps: number of steps to use when fading to 0.  More steps = longer fade time
	"""
	# number of steps to go from max to 0 for each color
	STEPS = numSteps
	
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
		setColor(1,[currentColors[0],currentColors[2],currentColors[4]])
		setColor(2,[currentColors[1],currentColors[3],currentColors[5]])
		time.sleep(0.02)
		#turn all the way off if reach the end
		#print "currentColors after iteration"
		#print currentColors
		#time.sleep(10)

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
	return;

def setPinValue(pin,value):
    """
    Turn a pin high
    Input: 
        pin = Pin number
        stauts = 0|1 (off|on)
    """
    pb.write(pin,value)
    #os.system("echo \"{0}={1}\" > /dev/pi-blaster" .format(pin,value))
    
def allOff():
	"""
	Turn all LEDs off
	"""
	setColor(1,[0,0,0])
	setColor(2,[0,0,0])
	return;

def dangerRange(distance,topOfRange):
	'''
	This function will flash red on/off while in the danger range
	Args:
	-- distance: the current range sensor distance
	-- topOfRange: the top end of the range to flash in
	'''
	while distance < topOfRange:
		FLASHSPEED = 0.01
		#turn LEDs all red
		t1 = threading.Thread(target=setColor,args=(1,[0,0,0]))
		t1.start()
		#t1.join()
		t2 = threading.Thread(target=setColor,args=(2,[0,0,0]))
		t2.start()
		#t2.join()
		time.sleep(FLASHSPEED)
		#Turn all LEDs off
		t1 = threading.Thread(target=setColor,args=(1,[1,0,0]))
		t1.start()
		#t1.join()
		t2 = threading.Thread(target=setColor,args=(2,[1,0,0]))
		t2.start()
		#t2.join()
		distance = rsDistance.measureAvg() 
	return distance

def fadeOutThreading(stepSize):
	for pin in ALL_GPIO_PINS:
		print pin
		t = threading.Thread(target=fadeOutLED3,args=(pin,1,stepSize))
		t.start()
		t.join
	return	
	
