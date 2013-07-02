#!/usr/bin/python
"""
@package rpiGpioPWM_test.py
Documentation for this module
"""

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
#PWM frequency
HZ = 100
#PWM Duty Cycle higher seems to smooth out fading

#GPIO.setup(18, GPIO.OUT) 
GPIO.setup(17, GPIO.OUT)


#r1 = GPIO.PWM(18, HZ)
r2 = GPIO.PWM(17, HZ)

#r1.start(0)
r2.start(100)
pause_time = 0.008

try:
    while True:
        for i in range(1,101):
#            r1.ChangeDutyCycle(i)
            r2.ChangeDutyCycle(100-i)
            sleep(pause_time)
        for i in range(100,-1,-1):
#            r1.ChangeDutyCycle(i)
            r2.ChangeDutyCycle(100 - i)
            sleep(pause_time)
            
except KeyboardInterrupt:
#    r1.stop()
    r2.stop()
    GPIO.cleanup()
