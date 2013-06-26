#!/usr/local/python
"""@package CommonLED

This class holds all common LED methods
"""
import Pblstr
from decimal import Decimal

class CommonLED():
	def __init__(self):
		self.GPIO_PINS_LED_1 = [2,5,7]
		self.GPIO_PINS_LED_2 = [1,4,6]
		self.pb = Pblstr.Pblstr()

	def setColor(self,ledStripNum,RGB):
        	"""
        	Set RGB color passed to it
        	LEDstrip: Which strip? (1|2)
        	RGB - array of R, G, B values to set
        	"""
        	#check which strip we want to do stuff to
        	if ledStripNum == 1:
                	gpioPinsList = self.GPIO_PINS_LED_1
        	elif ledStripNum == 2:
                	gpioPinsList = self.GPIO_PINS_LED_2
        	i = 0
        	for gpioVal in gpioPinsList:
                	self.pb.write(gpioVal, Decimal(RGB[i]))
                	#self.pb.write(gpioVal, RGB[i])
                	i += 1
        	return

	def setPinValue(self,pin,value):
    		"""
    		Turn a pin high
    		Input: 
        	pin = Pin number
       		stauts = 0|1 (off|on)
    		"""
    		self.pb.write(pin,value)

	def allOff(self):
        	"""
        	Turn all LEDs off
        	"""
        	self.setColor(1,[0,0,0])
        	self.setColor(2,[0,0,0])
        	#return

