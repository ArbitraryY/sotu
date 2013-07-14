#!/usr/bin/python

"""@package pltnGpio.py 

All GPIO functions.  This holds the master list of LED colors and their associated GPIO
Pin.  There are Methods to return allPins, a single pin, all pins from a single strip, or 
the pin values for a single color on both strips.
"""

from collections import OrderedDict

class pltnGpio():
    def __init__(self):
        """ Define dictionary of GPIO pins
        """
        self.gpioPins = OrderedDict()
        self.gpioPins['r1'] = '2'
        self.gpioPins['g1'] = '5'
        self.gpioPins['b1'] = '7'
        self.gpioPins['r2'] = '1'
        self.gpioPins['g2'] = '4'
        self.gpioPins['b2'] = '6'
        
    def getPin(self,colorStrip):
        """Get the value of a single pin from its colorStrip definition
            Input: 
                colorStrip = Color (represented by "r", "g", or "b") concatenated
                             with the strip number to activate it on (strip1 | strip2)
            Return: 
                pin = Its associated pin value
        """
        return self.gpioPins[colorStrip]
        
    def getStripPins(self,stripNum):
        """Get the pin values for strip (1|2)
            Input:
                stripNum = The strip to get the pins from
            Return: 
                pins = List of pins for given strip
        """
        #create r,g,b string values from arg stripNum as r1,g1,b1 or r2,g2,b2, etc
        r = "r"+str(stripNum)
        g = "g"+str(stripNum)
        b = "b"+str(stripNum)
        
        return [self.gpioPins[r],self.gpioPins[g],self.gpioPins[b]] 
    
    def getPinBothStrips(self,color):
        """Get the value of a both pins for <color>
            Input:
                color = r, g, or b
            Return: 
                pins = A list of pins that match the passed color
        """
        pinOne = color+str(1)
        pinTwo = color+str(2)
        
        return [self.gpioPins[pinOne],self.gpioPins[pinTwo]]
    
    def getAllPins(self,option):
        """Get all of the GPIO pins
            Input: None
            Return:
                pins = All GPIO pins
        """
        #return list of all GPIO pins
        if option == 'asList':
            return self.gpioPins.values()
        elif option == 'asDict':
            return self.gpioPins
        else:
            print "not a valid option"
