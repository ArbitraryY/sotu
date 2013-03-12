#!/usr/bin/python

# Import required Python libraries
import RPi.GPIO as GPIO
import time as time
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO to use on Pi
GPIO_PWM =22; 
 
# Set pin as input
GPIO.setup(GPIO_PWM,GPIO.IN)      # Echo
 
def measure():
  # This function measures a distance
  
  start = time.time()
  while GPIO.input(GPIO_PWM)==0:
    start = time.time()
  
  while GPIO.input(GPIO_PWM)==1:
    stop = time.time()

  elapsed = stop-start
  #distance = (elapsed * 34300)/2 #speed of sound in cm/sec
  distance = (elapsed * 13512)/2 #speed of sound in in/sec

  return distance

def measureAvg():
  # This function takes 3 measurements and
  # returns the average.

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
 
    # Read PIR state
    Current_State = GPIO.input(GPIO_PWM)
    print Current_State 
    #Call distance Avg function
    distance = measure()
    print "Distance : %.1f" % distance
    time.sleep(1)

except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()
