#!/bin/bash

#start OSCServer
perl /home/projects/platoon/OSCServer.pl 
sleep 2
ps -eaf | grep OSCServer.pl
sleep 5
#start pi-blaster; PWM all GPIOs
sudo /home/pi/pi-blaster
sleep 2
ps -eaf | grep pi-blaster
sleep 5
#start range sensor script
sudo /home/projects/platoon/rangeSensor.py
sleep 2
ps -eaf | grep rangeSensor.py
sleep 5

