#!/bin/bash

RELEASE_DIR=/usr/local/pltn_test
DEV_HOME=/home/pltn/platoon

#Copy OSC related files
echo
echo "Copying OSC files to release directory" 
echo
sudo cp -r $DEV_HOME/OSC/* $RELEASE_DIR/OSC

#Do rangeSensor stuff
cd $DEV_HOME/rangeSensor
echo
echo "compiling rangeSensor Python Scripts"
echo 
python -m compileall .
echo
echo "Copying rangeSensor Python Scripts to release directory" 
echo
sudo cp $DEV_HOME/rangeSensor/*.pyc $RELEASE_DIR/rangeSensor

#Copy Scripts
sudo cp $DEV_HOME/scripts/init/* $RELEASE_DIR/scripts


