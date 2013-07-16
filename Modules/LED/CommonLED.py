#!/usr/local/python
"""@package CommonLED

This class holds all common LED methods
"""
import sys
sys.path.append("/usr/local/pltn/Modules")

from Pblstr import Pblstr
from decimal import Decimal,getcontext
from time import sleep
from pltnGpio import pltnGpio

getcontext().prec = 2

class CommonLED():
	def __init__(self):
		self.pg              = pltnGpio.pltnGpio() 
		self.pb              = Pblstr.Pblstr()
		self.stepSize        = 0.05 #STEP Size for fading out 
		
	def analogToDigital(self,analogColors):
		"""Converts RGB analog values to Digital for pi-blaster
			Input: 
				analogColors: 2D list of analog RGB valueslors) and converts them to digital.
			Return: 2D list of digital RGB values (digitalColors)
		"""
		digitalColors = [[Decimal(x)/Decimal(255) for x in y] for y in analogColors]
		return digitalColors

	def setColor(self,ledStripNum,RGB):
        	"""Set RGB color passed to it
        	LEDstrip: Which strip? (1|2)
        	RGB - array of R, G, B values to set
        	"""
        	#check which strip we want to do stuff to
        	if ledStripNum == 1:
                	gpioPinsList = self.pg.getStripPins(1)
        	elif ledStripNum == 2:
                	gpioPinsList = self.pg.getStripPins(2)
        	i = 0
        	for gpioVal in gpioPinsList:
                	self.pb.write(gpioVal, Decimal(RGB[i]))
                	i += 1
        	return

	def setPinValue(self,pin,value):
    		"""Turn a pin high
    			Input: 
        			pin = Pin number
       				status = 0|1 (off|on)
       			Return: None
    		"""
    		self.pb.write(pin,value)

	def allOff(self):
        	"""Turn all LEDs off
        	"""
        	self.setColor(1,[0,0,0])
        	self.setColor(2,[0,0,0])
	
	def ledFlashFade(self, gpioPin, pinValue):
		"""Turn an LED on then fade it out immediately
			Input:
				gpioPin: GPIO pin to turn on
				pinValue: Value to set the pin to (per pi-blaster 0 - 1)
			Return: None 
		"""
		self.fadeOutSinglePin(gpioPin, pinValue,self.stepSize)
	
	def flash(self,gpioPin,sleepTime):
		"""Turn an LED on then off immediately
			Input:
				gpioPin: GPIO pin to turn on then off
			Return: None
		"""
		self.setPinValue(gpioPin,1)
		sleep(sleepTime)
		self.setPinValue(gpioPin,0)
			
	def fadeOutSinglePin(self, gpioPinVal, currentVal, stepSize):
		'''This function takes a GPIO pin value and a current LED color
		   value and fades it out completely
		   Input:
		   		gpioPinVal: Pin to fade out
		   		currentVal: Fade from this value to 0
		   		stepSize: Size of value to step down from currentVal
	   		Return: None 
		'''
		while currentVal > 0.00:
			self.pb.write(gpioPinVal,currentVal)
			currentVal -= stepSize;
			#set to zero once it gets negative
			if currentVal < 0.00:
				self.pb.write(gpioPinVal,0)
				#set current colors to zero before exiting loop
				currentVal = 0.00
			print "%0.2f" % currentVal