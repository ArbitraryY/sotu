#!/bin/bash

RELEASE_DIR=/usr/local/pltn
DEV_HOME=/home/pltn/platoon

#Copy OSC related files
echo
echo "Copying OSC files to release directory" 
echo
cp $DEV_HOME/OSC/* $RELEASE_DIR/OSC

#Do rangeSensor stuffcompile .py files
cd $DEV_HOME/rangeSensor
echo
echo "compiling rangeSensor Python Scripts"
echo 
python -m compileall .
echo
echo "Copying rangeSensor Python Scripts to release directory" 
echo
cp $DEV_HOME/*.pyc $RELEASE_DIR/rangeSensor

