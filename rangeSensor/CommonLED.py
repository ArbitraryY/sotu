#!/usr/local/python
"""@package CommonLED

This class holds all common LED methods
"""
import Pblstr
from decimal import Decimal,getcontext

getcontext().prec = 2

class CommonLED():
	def __init__(self):
		self.GPIO_PINS_LED_1 = [2,5,7]
		self.GPIO_PINS_LED_2 = [1,4,6]
		self.pb              = Pblstr.Pblstr()
		self.stepSize        = Decimal(0.05) 

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
	
	def ledFlashFade(self):
		self.setPinValue(self.GPIO_PINS_LED_1[1],1)
		self.fadeOutSinglePin(self.GPIO_PINS_LED_1[1],1,self.stepSize)
	
	def fadeOutSinglePin(self, gpioPinVal, currentVal, stepSize):
		'''
		This function takes a GPIO pin value and a current LED color
		value and fades it out completely 
		'''
		print "hello from thread: %i" % gpioPinVal
		print "fading out now"
		STEP = Decimal(stepSize)
		while currentVal > Decimal(0.00):
			self.pb.write(gpioPinVal,currentVal)
			currentVal -= Decimal(STEP);
			#set to zero once it gets negative
			if currentVal < Decimal(0):
				self.pb.write(gpioPinVal,0)
				#set current colors to zero before exiting loop
				currentVal = 0
			print "%0.2f" % currentVal

