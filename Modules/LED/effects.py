#!/usr/local/python
"""@package effects

This class holds all LED effects
"""
import sys
sys.path.append("/usr/local/pltn/Modules")

#from Pblstr import Pblstr
from decimal import Decimal,getcontext
from time import sleep
from pltnGpio import pltnGpio
from LED import CommonLED

getcontext().prec = 2

class effects():
	def __init__(self):
		self.pg              = pltnGpio.pltnGpio()
		self.cLED			 = CommonLED.CommonLED()

	def fadeUp(self,startColor,endColor,stepSize,fadeSpeed):
		endR = endColor[0]
		endG = endColor[1]
		endB = endColor[2]
		stR = startColor[0]
		stG = startColor[1]
		stB = startColor[2]
		rFlag,gFlag,bFlag = 'start'
		
		while rFlag != 'stop' and gFlag != 'stop' and bFlag !='stop':
			print "-----------------"
			print stR
			print stG
			print stB
			print "-----------------"
			if stR < endR:
				stR += stepSize;
			else:
				rFlag = 'stop'
			if stG < endG:
				stG += stepSize;
			else:
				gFlag = 'stop'
			if stB < endB:
				stB += stepSize;
			else:
				bFlag = 'stop'
			sleep(fadeSpeed)
	
	def pulse(self,RGB,pulseInc,pulseTime,steps,stepSize):
		"""Pulses the LEDs
			Input: 
				RGB: List of colors in RGB format
				pulseInc (secs): Time increment between change from color value to the next
					- EX. 255,255,255 -> 254,254,254 <wait pulseTime> 254,254,254 -> 253,253,253
				pulseTime: How many times to do iterations of the pulse 
				steps: # of steps to go down before coming back up to original color
				stepSize: How much to jump to next value (0 - 1)
					Note the constraint on the step variables: 
						- steps*stepSize < Lowest value in RGB
			Return: None				
		"""
		self.cLED.setColor(1,RGB)
		self.cLED.setColor(2,RGB)
		#stepSize = 0.01
		while pulseTime > 0:
			cR = RGB[0]
			cG = RGB[1]
			cB = RGB[2]
			#print "++++++++++++++++++"				
			#print cR
			#print cG
			#print cB
			#print "++++++++++++++++++"
			for x in range(0,steps):
				self.cLED.setPinValue(self.pg.getPin('r1'),cR)
				self.cLED.setPinValue(self.pg.getPin('r2'),cR)
				#sleep(pulseInc)
				self.cLED.setPinValue(self.pg.getPin('g1'),cG)
				self.cLED.setPinValue(self.pg.getPin('g2'),cG)
				#sleep(pulseInc)
				self.cLED.setPinValue(self.pg.getPin('b1'),cB)
				self.cLED.setPinValue(self.pg.getPin('b2'),cB)
				#sleep(pulseInc)
				cR -= stepSize
				cG -= stepSize
				cB -= stepSize
				#print "================="				
				#print cR
				#print cG
				#print cB
				#print "================="				
			sleep(pulseInc)
			
			for x in range(0,steps):
				self.cLED.setPinValue(self.pg.getPin('r1'),cR)
				self.cLED.setPinValue(self.pg.getPin('r2'),cR)
			#	sleep(pulseInc)
				self.cLED.setPinValue(self.pg.getPin('g1'),cG)
				self.cLED.setPinValue(self.pg.getPin('g2'),cG)
			#	sleep(pulseInc)
				self.cLED.setPinValue(self.pg.getPin('b1'),cB)
				self.cLED.setPinValue(self.pg.getPin('b2'),cB)
			#	sleep(pulseInc)
				cR += stepSize
				cG += stepSize
				cB += stepSize
			#	print "-----------------"				
			#	print cR
			#	print cG
			#	print cB
			#	print "-----------------"				
			sleep(pulseInc)
			
			pulseTime = pulseTime - 1
			print pulseTime
								
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