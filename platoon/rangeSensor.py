#!/usr/bin/python

# Import required Python libraries
import RPi.GPIO as GPIO
import time as time
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO to use on Pi
GPIO_PIR = 22;
 
print "PIR Module Test (CTRL-C to exit)"
 
# Set pin as input
#GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo
 
try:
 
  print "Waiting for sensor to settle ..."
 
  # Loop until users quits with CTRL-C
  while True :
 
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
 
    print Current_State 
    time.sleep(1)
except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()
