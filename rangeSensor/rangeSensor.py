#!/usr/bin/python
"""@package rangeSensor

This module controls the rangeSensor LED programming
"""
import sys
sys.path.append("/usr/local/pltn/Modules")

import threading
from decimal import Decimal,getcontext
#import RPi.GPIO as GPIO
from time import sleep
import os
from rsDistance import rsDistance
from LED import LED
from LED import CommonLED
from pltnGpio import pltnGpio

#instantiate objects
cLED = CommonLED.CommonLED()
pg = pltnGpio.pltnGpio()
#set Decimal precision to 2 places
getcontext().prec = 2

#define the GPIO pins for each strip
GPIO_PINS_LED_1 = pg.getStripPins(1)
GPIO_PINS_LED_2 = pg.getStripPins(2)
#ALL_GPIO_PINS   = [2,1,5,4,7,6]

#set mode to BCM so PWM
#GPIO.setmode(GPIO.BCM)
 
# Set range sensor pin as an input. Need thisin order to overtake the setting
# from pi-blaster which sets all GPIO pins to input
#GPIO.setup(GPIO_RS,GPIO.IN) 
 
#define global step size for fading theough colors
global FADESPEED
global STEP

#Increase to slow down LED color changes
FADESPEED = Decimal(0.02)
#step size to jump to the next RGB value when fading.
#decreasing this will slow down the fade
STEP = Decimal(0.01)

# define Analog LED RGB colors
RNG_1_LED_1_ANALOG = [ [28,30,68],[40,93,144],[255,255,255],[40,93,144],[123,32,144],[67,47,103] ]
RNG_1_LED_2_ANALOG = [ [150,44,37],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]
#RNG_2_LED_1_ANALOG = [ [0,0,0],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]
#RNG_2_LED_2_ANALOG = [ [150,44,37],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]
#RNG_3_LED_1_ANALOG = [ [150,44,37],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]
#RNG_3_LED_2_ANALOG = [ [150,44,37],[32,69,97],[121,65,137],[121,65,137],[238,68,79] ]

#Convert Analog RGB values to Digital
RNG_1_LED_1 = LED.analogToDigital(RNG_1_LED_1_ANALOG)
RNG_1_LED_2 = LED.analogToDigital(RNG_1_LED_2_ANALOG)
#RNG_2_LED_1 = analogToDigital(RNG_1_LED_2_ANALOG)
#RNG_2_LED_2 = analogToDigital(RNG_1_LED_2_ANALOG)
#RNG_3_LED_1 = analogToDigital(RNG_1_LED_2_ANALOG)
#RNG_3_LED_2 = analogToDigital(RNG_1_LED_2_ANALOG)

#define ranges
#ranges=[10.0,16.0,17.0,47.0,48.0,70.0];
ranges=[20.0,100.0];

try:
    print "Waiting for sensor to settle ..."
    sleep(0.1)
    # Loop until users quits with CTRL-C
    #turn off all LEDs when starts
    cLED.allOff()
    while True : 
        i = 0
        j = i + 1
        k = 0
        m = k + 1
        #take a distance measurement
        distance = rsDistance.measureAvg()
        print "Average Distance : %.1f" % distance
        #check which range we are in
        while distance < ranges[0]:
           distance = LED.dangerRange(distance,ranges[0])
           #print "distance  in dangerRange: %.2f" % distance
           #time.sleep(10)          
            
        #set initial LED colors fadeIn function will replace this when written
        if distance >= ranges[0] and distance <= ranges[1]:
            rangeVal = 1;
            cLED.setColor(1,RNG_1_LED_1[0])
            cLED.setColor(2,RNG_1_LED_2[0])
            #Holds all currently set colors.  This will be passed to fadeIn/Out functions
            currentColors = [RNG_1_LED_1[0][0],RNG_1_LED_2[0][0],RNG_1_LED_1[0][1],RNG_1_LED_2[0][1],RNG_1_LED_1[0][2],RNG_1_LED_2[0][2]]
            #fadeInLed(currentColors)
        #elif distance >= ranges[2] and distance <= ranges[3]:
        #elif distance >= ranges[4] and distance <= ranges[5]:
        while distance >= ranges[0] and distance <= ranges[1]:
            
            rangeVal = 1;
            
            print "------------ In Range 1-----------"
            #determine the number of colors in each array
            LED_1_COLORS_LENGTH = len(RNG_1_LED_1)
            LED_2_COLORS_LENGTH = len(RNG_1_LED_2)
            
            #measure distance again and exit loop if out of range
            #distance = rsDistance.measureAvg()
            #print "distance in loop: %.3f" % distance
            '''
            if distance < ranges[0] or distance > ranges[1]:
                #LED.allOff()
                LED.fadeOutLED(currentColors)
                break
            '''
            #fade red LEDs
            if(rangeVal):
                rangeVal, currentColors[0] = LED.fadeLED(GPIO_PINS_LED_1[0],RNG_1_LED_1[i][0],RNG_1_LED_1[j][0],ranges[0],ranges[1],STEP,FADESPEED)
            if(rangeVal):
                rangeVal, currentColors[1] = LED.fadeLED(GPIO_PINS_LED_2[0],RNG_1_LED_2[k][0],RNG_1_LED_2[m][0],ranges[0],ranges[1],STEP,FADESPEED)
            #fade green LEDs
            if(rangeVal):
                rangeVal, currentColors[2] = LED.fadeLED(GPIO_PINS_LED_1[1],RNG_1_LED_1[i][1],RNG_1_LED_1[j][1],ranges[0],ranges[1],STEP,FADESPEED)
            if(rangeVal):
                rangeVal, currentColors[3] = LED.fadeLED(GPIO_PINS_LED_2[1],RNG_1_LED_2[k][1],RNG_1_LED_2[m][1],ranges[0],ranges[1],STEP,FADESPEED)	
            #fade blue LEDs
            if(rangeVal):
                rangeVal, currentColors[4] = LED.fadeLED(GPIO_PINS_LED_1[2],RNG_1_LED_1[i][2],RNG_1_LED_1[j][2],ranges[0],ranges[1],STEP,FADESPEED)
            if(rangeVal):
                rangeVal, currentColors[5] = LED.fadeLED(GPIO_PINS_LED_2[2],RNG_1_LED_2[k][2],RNG_1_LED_2[m][2],ranges[0],ranges[1],STEP,FADESPEED)
            #print "This is the rangeVal after fade block: %i", rangeVal
            #print "This is the distance after fading LEDs: %f" % distance
            '''
            if(rangeVal):
                #fade red LEDs
                pThread0 = threading.Thread( target=LED.fadeLED, args=[GPIO_PINS_LED_1[0],RNG_1_LED_1[i][0],RNG_1_LED_1[j][0],ranges[0],ranges[1],STEP,FADESPEED,q0])
                rangeVal, currentColors[0] = q0.get()
                pThread0.join()
                print "red1:{0}, {1}" .format(rangeVal, currentColors[0])   
                
                pThread1 = threading.Thread( target=LED.fadeLED, args=[GPIO_PINS_LED_2[0],RNG_1_LED_2[k][0],RNG_1_LED_2[m][0],ranges[0],ranges[1],STEP,FADESPEED,q1])
                rangeVal, currentColors[1] = q1.get()
                pThread1.join()
                print "red2:{0}, {1}" .format(rangeVal, currentColors[1]) 
                #fade green LEDs
                pThread2 = threading.Thread( target=LED.fadeLED, args=[GPIO_PINS_LED_1[1],RNG_1_LED_1[i][1],RNG_1_LED_1[j][1],ranges[0],ranges[1],STEP,FADESPEED,q2])
                rangeVal, currentColors[2] = q2.get()
                pThread2.join()
                print "green 1:{0}, {1}" .format(rangeVal, currentColors[2]) 
                
                pThread3 = threading.Thread( target=LED.fadeLED, args=[GPIO_PINS_LED_1[1],RNG_1_LED_1[i][1],RNG_1_LED_1[j][1],ranges[0],ranges[1],STEP,FADESPEED,q3])
                rangeVal, currentColors[3] = q3.get()
                pThread3.join()
                print "green 2:{0}, {1}" .format(rangeVal, currentColors[3]) 
                
                #fade blue LEDs
                pThread4 = threading.Thread( target=LED.fadeLED, args=[GPIO_PINS_LED_1[2],RNG_1_LED_1[i][2],RNG_1_LED_1[j][2],ranges[0],ranges[1],STEP,FADESPEED,q4])
                rangeVal, currentColors[4] = q4.get()
                pThread4.join()
                print "blue 1:{0}, {1}" .format(rangeVal, currentColors[4]) 
                
                pThread5 = threading.Thread( target=LED.fadeLED, args=[GPIO_PINS_LED_2[2],RNG_1_LED_2[k][2],RNG_1_LED_2[m][2],ranges[0],ranges[1],STEP,FADESPEED,q5])
                rangeVal, currentColors[5] = q5.get()
                pThread5.join()
                print "blue 2:{0}, {1}" .format(rangeVal, currentColors[5]) 
            '''
            #if out of range (i.e. rangeVal = 0) then fade out
            print "rangeVal32: %s" % rangeVal
            '''
            if(rangeVal == 0):
                for i in range(len(ALL_GPIO_PINS)):
                    #LED.fadeOutLED3(ALL_GPIO_PINS[i],currentColors[i])
                    threading.Thread(target=LED.fadeOutLED3, args=[ALL_GPIO_PINS[i],currentColors[i]]).start()
                    currentColors[i] = 0
                    print i
            '''
            if(rangeVal == 0):
                LED.dangerRange(distance,ranges[0])
            elif(rangeVal == 2):
                LED.fadeOutLED2(currentColors,distance)
            '''
            if(rangeVal == 0):
                #LED.fadeOutLED(currentColors)
                LED.fadeOutLED2(currentColors,distance)
            '''
            #Color rotation logic
            if i < (LED_1_COLORS_LENGTH - 1):
                i += 1
            elif i == (LED_1_COLORS_LENGTH - 1):
                i = 0
            if j < (LED_1_COLORS_LENGTH - 1):
                j += 1
            elif j == (LED_1_COLORS_LENGTH - 1):
                j = 0
            if k < (LED_2_COLORS_LENGTH - 1):
                k += 1
            elif k == (LED_2_COLORS_LENGTH - 1):
                k = 0
            if m < (LED_2_COLORS_LENGTH - 1):
                m += 1
            elif m == (LED_2_COLORS_LENGTH - 1):
                m = 0
            #take a distance measurement to make sure since still in while
            # that we need to exit it
            distance = rsDistance.measureAvg()
            print "distance after fading out: %0.2f" % distance
            
            
            #print 'At end of one fade'
            #print currentColors
            #time.sleep(3000)
	'''
	elif distance >= ranges[2] and distance <= ranges[3]:
		print "------------Range 2-----------"
	elif distance >= ranges[4] and distance <= ranges[5]:
		print "------------Range 3-----------"
	else
		print "not in range"
	'''

    # time between measurements
    	sleep(0.01)

except KeyboardInterrupt:
    cLED.allOff()
    print "  Quit"
    # Reset GPIO settings
    #GPIO.cleanup()
