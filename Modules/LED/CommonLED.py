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
		self.pg = pltnGpio.pltnGpio() 
		self.pb = Pblstr.Pblstr()
		
	def aToD(self,analogColor):
		"""This function takes an RGB analog value and converts it to digital
			Input:
				analogColor(int): An analog color value (0 - 255)
			Return:
				Digital color value to two decimal places (0.00 - 1.00) 
		"""
		return Decimal(analogColor)/Decimal(255)
	
	def analogToDigital(self,analogColors):
		"""Converts RGB analog values to Digital for pi-blaster
			Input: 
				analogColors: 2D list of analog RGB values) and converts them to digital.
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