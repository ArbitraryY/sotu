#!/usr/bin/python

import RPi.GPIO as GPIO
import time as time
 
GPIO.setmode(GPIO.BCM)
 
# Define GPIO to use for PWM
GPIO_PWM =22; 
 
# Set pin as input
GPIO.setup(GPIO_PWM,GPIO.IN) 
 
def measure():
  # Measures a distance (time it takes to go from 0 --> or 1 --> 0)
  
  start = time.time()
  while GPIO.input(GPIO_PWM)==0:
    start = time.time()
  
  while GPIO.input(GPIO_PWM)==1:
    stop = time.time()

  elapsedTime = stop-start
  #distance = (elapsed * 34300)/2 #speed of sound in cm/sec
  distance = (elapsedTime * 13512)/2 #speed of sound in in/sec

  return distance

def measureAvg():
  # Take 3 measurements and return the average. Should make for more reliable readings

  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

try:
 
  print "Waiting for sensor to settle ..."
 
  # Loop until users quits with CTRL-C
  while True :
 
    # Read and print sensor state
    Current_State = GPIO.input(GPIO_PWM)
    print Current_State 
    #Call distance Avg function
    distance = measure()
    print "Distance : %.1f" % distance
    # time between measurments
    time.sleep(1)

except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()
