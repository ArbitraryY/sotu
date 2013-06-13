#!/usr/bin/python
"""
@package rpiGpioPWM_test.py
Documentation for this module
"""

import RPi.GPIO as GPIO
import time

#PWM frequency
HZ = 100
#PWM Duty Cycle higher seems to smooth out fading
DUTYCYCLE = 90
FADESPEED = 0.002

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

try:
    while True:
        #fade in
        for i in range(101):
            for j in range(len(gpioPinsList)):
                gpioPinsObjs[j].start(0 + i) 
                time.sleep(FADESPEED)

        #fade out
        for i in range(101):
            for j in range(len(gpioPinsList)):
                gpioPinsObjs[j].start(100 - i) 
                time.sleep(FADESPEED)

except:
    GPIO.cleanup()
    pass