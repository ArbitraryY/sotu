#!/usr/bin/python
"""
@package rpiGpioPWM_test.py
Documentation for this module
    This version is specifically for the wndwPlay display
"""

import RPi.GPIO as GPIO
import time
from random import randrange


#PWM frequency
HZ = 100
#PWM Duty Cycle higher seems to smooth out fading
DUTYCYCLE = 90
FADESPEED = 0.0005
FADESPEEDSINGLE = 0.005

GPIO.setmode(GPIO.BCM)

gpioPinsList = [["r1",18],["g1",23],["b1",25],["r2",17],["g2",22],["b2",24]]
gpioPinsObjs = []

#setup GPIO pins as outputs and create PWM objects for each
for i in range(len(gpioPinsList)):
    GPIO.setup(gpioPinsList[i][1], GPIO.OUT)
    gpioPinsObjs.append(GPIO.PWM(gpioPinsList[i][1], HZ))
    
#Set the duty cycle for each pin
for i in range(len(gpioPinsList)):
    gpioPinsObjs[i].ChangeDutyCycle(DUTYCYCLE)

#fade in
def fadeTweet():
    for j in range(len(gpioPinsList)):
        gpioPinsObjs[j].start(100)

    time.sleep(1)
        #fade out
    for i in range(101):
        for j in range(len(gpioPinsList)):
            gpioPinsObjs[j].start(100 - i)
            time.sleep(FADESPEED)
    #for j in range(len(gpioPinsList)):
     #       gpioPinsObjs[j].stop

def fadeRed():
    gpioPinsObjs[0].start(100)
    gpioPinsObjs[3].start(100)
    time.sleep(1)
    for i in range(101):
        gpioPinsObjs[0].start(100 - i)
        gpioPinsObjs[3].start(100 - i)
        time.sleep(FADESPEEDSINGLE)
    
def fadeGreen():
    gpioPinsObjs[1].start(100)
    gpioPinsObjs[4].start(100)
    time.sleep(1)
    for i in range(101):
        gpioPinsObjs[1].start(100 - i)
        gpioPinsObjs[4].start(100 - i)
        time.sleep(FADESPEEDSINGLE)

def fadeBlue():
    gpioPinsObjs[2].start(100)
    gpioPinsObjs[5].start(100)
    time.sleep(1)
    for i in range(101):
        gpioPinsObjs[2].start(100 - i)
        gpioPinsObjs[5].start(100 - i)
        time.sleep(FADESPEEDSINGLE)
        
def scatter():
    for i in range(10):
        randPin = randrange(6)
        gpioPinsObjs[randPin].start(100)
        for i in range (101):
            gpioPinsObjs[randPin].start(100 - i)
            time.sleep(0.003)

def gpioClean():
    GPIO.cleanup()
    return