#!/bin/bash

PROJECT_PATH=/home/pi/projects/platoon

#start OSCServer
perl ${PROJECT_PATH}/OSCserver.pl &
sleep 2
ps -eaf | grep OSCserver.pl
sleep 5
#start pi-blaster; PWM all GPIOs
sudo /home/pi/pi-blaster
sleep 2
ps -eaf | grep pi-blaster
sleep 5
#start range sensor script
sudo ${PROJECT_PATH}/rangeSensor.py &
sleep 2
ps -eaf | grep rangeSensor.py
sleep 5

