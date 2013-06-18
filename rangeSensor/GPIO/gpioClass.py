#!/usr/bin/python

"""@package GPIO
Documentation for this module
"""

import RPi.GPIO as GPIO

class gpioClass:
    gpioPinsList = [["r1",18],
                    ["g1",23],
                    ["b1",25],
                    ["r2",17],
                    ["g2",22],
                    ["b2",24]]
    #PWM frequency
    HZ = 100 
    #PWM Duty Cycle higher seems to smooth out fading
    DUTYCYCLE = 90
    
    def __init__(self):
        """
        Set GPIO mode to BCM
        """
        GPIO.setmode(GPIO.BCM)
        self.gpioPinsObjs = []
        #set each pin as an output and create corresponding object
        for i in range(len(gpioClass.gpioPinsList)):
            GPIO.setup(gpioClass.gpioPinsList[i][1], GPIO.OUT)
            self.gpioPinsObjs.append(GPIO.PWM(gpioClass.gpioPinsList[i][1], gpioClass.HZ))
        #Set the duty cycle for each pin
        #for i in range(len(gpioClass.gpioPinsList)):
         #   self.gpioPinsObjs[i].ChangeDutyCycle(gpioClass.DUTYCYCLE)
    
    def getGpioObj(self,pin):
        """
        
        Return: List of GPIO Pin Objects used by RPi.GPIO
        """
        #list for pin objects
        return self.gpioPinsObjs[pin]
    
    def gpioClean(self):
        """
        Clean up the GPIO pins
        """
        GPIO.cleanup()
        return