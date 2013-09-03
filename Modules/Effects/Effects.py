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
from CommonLED import CommonLED

getcontext().prec = 2

class Effects():
	def __init__(self):
		self.pg   = pltnGpio.pltnGpio()
		self.cLED = CommonLED.CommonLED()
		self.RGBLength = 3

	def rotateColors(self,analogColors,numRots,stepSize,fadeSpeed):
		"""This function rotates the LEDs between a predefined list of colors
			Input: 
				colors: 2D list of RGB colors as [(r,g,b),(r,g,b)] in analog values
				numRots: Int - Number of times to rotate through colors
				stepSize: The size of the step between colors
				fadeSpeed: Controls the speed of the fade (higher = slower fading)
			Return: None 
		"""
		iter = 0
		i = 0
		j = i + 1
		#the number of colors passed to rotate between
		numColors = len(analogColors)
		while iter != numRots:
			self.fadeColor(analogColors[i],analogColors[j],stepSize,fadeSpeed)
			
			#fade logic	
			if i < numColors - 1:
				i += 1
			else:
				i = 0
			#Check if last color has been faded to. If so that counts
			#as an iteration through
			if j == numColors-1:
				iter += 1
			if j < numColors - 1:
				j += 1
			else:
				j = 0
				
				
		
			
	def fadeColor(self,startColor,endColor,stepSize,fadeSpeed):
		"""This function fades up or down from one color to another
			Input:
				startColor: List of RGB values to start the fade from
				endColor: List of RGB values to stop the fade at
				stepSize: The size of the step between colors
				fadeSpeed: Controls the speed of the fade (higher = slower fading)
			Return: None
		"""
		endR = endColor[0]
		endG = endColor[1]
		endB = endColor[2]
		stR = startColor[0]
		stG = startColor[1]
		stB = startColor[2]
		
		rFlag = gFlag = bFlag = 'start'
		"""
		currentRGB = [startColor[0],startColor[1],startColor[2]]
		RGBFlags   = ['on','on','on']
		
		while RGBFlags[0] != 'stop' or RGBFlags[1] != 'stop' or RGBFlags[2] != 'stop':
			#2 is the Length of RGB array
			for i in range(3):
				if startColor[i] < endColor[i]:
					currentRGB[i] += stepSize
				elif startColor[i] > endColor[i]:
					currentRGB[i] -= stepSize
				elif startColor[i] == endColor[i]:
					RGBFlags[i] = 'stop'
					
			print '----------------------'
			for i in range(3):
				print "{0},{1},{2}" .format(i,self.cLED.aToD(currentRGB[i]),RGBFlags[i])
			
			print '----------------------'
			
			self.cLED.setColor(1,[self.cLED.aToD(currentRGB[0]),self.cLED.aToD(currentRGB[1]),self.cLED.aToD(currentRGB[2])])
			self.cLED.setColor(2,[self.cLED.aToD(currentRGB[0]),self.cLED.aToD(currentRGB[1]),self.cLED.aToD(currentRGB[2])])
			"""	
				
		while rFlag != 'stop' or gFlag != 'stop' or bFlag !='stop':
			#fade each pin one increment at a time
			if stR < endR:
				stR += stepSize;
			elif stR > endR:
				stR -= stepSize
			else:
				rFlag = 'stop'
			if stG < endG:
				stG += stepSize;
			elif stG > endG:
				stG -= stepSize
			else:
				gFlag = 'stop'
			if stB < endB:
				stB += stepSize;
			elif stB > endB:
				stB -= stepSize
			else:
				bFlag = 'stop'
			self.cLED.setColor(1,[self.cLED.aToD(stR),self.cLED.aToD(stG),self.cLED.aToD(stB)])
			self.cLED.setColor(2,[self.cLED.aToD(stR),self.cLED.aToD(stG),self.cLED.aToD(stB)])
			#self.cLED.setPinValue(self.pg.getPin('r1'),self.cLED.aToD(stR))
			#self.cLED.setPinValue(self.pg.getPin('r2'),self.cLED.aToD(stR))
			#self.cLED.setPinValue(self.pg.getPin('g1'),self.cLED.aToD(stG))
			#self.cLED.setPinValue(self.pg.getPin('g2'),self.cLED.aToD(stG))
			#self.cLED.setPinValue(self.pg.getPin('b1'),self.cLED.aToD(stB))
			#self.cLED.setPinValue(self.pg.getPin('b2'),self.cLED.aToD(stB))
			print "-----------------"
			print stR
			print stG
			print stB
			print "-----------------"
			print rFlag
			print gFlag
			print bFlag
			print "-----------------"
			#sleep(fadeSpeed)
	
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
		dRGB = self.cLED.aToDList(RGB)
		
		self.cLED.setColor(1,dRGB)
		self.cLED.setColor(2,dRGB)
		#stepSize = 0.01
		while pulseTime > 0:
			cR = RGB[0]
			cG = RGB[1]
			cB = RGB[2]
			print "++++++++++++++++++"				
			print cR
			print cG
			print cB
			print "++++++++++++++++++"
			for x in range(0,steps):
				self.cLED.setPinValue(self.pg.getPin('r1'),self.cLED.aToD(cR))
				self.cLED.setPinValue(self.pg.getPin('r2'),self.cLED.aToD(cR))
				#sleep(pulseInc)
				self.cLED.setPinValue(self.pg.getPin('g1'),self.cLED.aToD(cG))
				self.cLED.setPinValue(self.pg.getPin('g2'),self.cLED.aToD(cG))
				#sleep(pulseInc)
				self.cLED.setPinValue(self.pg.getPin('b1'),self.cLED.aToD(cB))
				self.cLED.setPinValue(self.pg.getPin('b2'),self.cLED.aToD(cB))
				#sleep(pulseInc)
				cR -= stepSize
				cG -= stepSize
				cB -= stepSize
				print "================="				
				print cR
				print cG
				print cB
				print "================="				
			sleep(pulseInc)
			
			for x in range(0,steps):
				self.cLED.setPinValue(self.pg.getPin('r1'),self.cLED.aToD(cR))
				self.cLED.setPinValue(self.pg.getPin('r2'),self.cLED.aToD(cR))
			#	sleep(pulseInc)
				self.cLED.setPinValue(self.pg.getPin('g1'),self.cLED.aToD(cG))
				self.cLED.setPinValue(self.pg.getPin('g2'),self.cLED.aToD(cG))
			#	sleep(pulseInc)
				self.cLED.setPinValue(self.pg.getPin('b1'),self.cLED.aToD(cB))
				self.cLED.setPinValue(self.pg.getPin('b2'),self.cLED.aToD(cB))
			#	sleep(pulseInc)
				cR += stepSize
				cG += stepSize
				cB += stepSize
				print "-----------------"				
				print cR
				print cG
				print cB
				print "-----------------"				
			sleep(pulseInc)
			
			pulseTime = pulseTime - 1
			print pulseTime
								
	def ledFlashFade(self, gpioPin, pinValue,stepSize):
		"""Turn an LED on then fade it out immediately
			Input:
				gpioPin: GPIO pin to turn on
				pinValue: Value to set the pin to (per pi-blaster 0 - 1)
			Return: None 
		"""
		self.fadeOutSinglePin(gpioPin, pinValue,stepSize)
	
	def flash(self,gpioPin,sleepTime):
		"""Turn an LED on then off immediately
			Input:
				gpioPin: GPIO pin to turn on then off
			Return: None
		"""
		self.cLED.setPinValue(gpioPin,1)
		sleep(sleepTime)
		self.cLED.setPinValue(gpioPin,0)
			
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
			self.cLED.setPinValue(gpioPinVal,currentVal)
			currentVal -= stepSize;
			#set to zero once it gets negative
			if currentVal < 0.00:
				self.cLED.setPinValue(gpioPinVal,0)
				#set current colors to zero before exiting loop
				currentVal = 0.00
			print "%0.2f" % currentVal