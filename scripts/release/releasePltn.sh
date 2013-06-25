#!/bin/bash

RELEASE_DIR=/usr/local/pltn
DEV_HOME=/home/pltn/platoon

#Copy OSC related files
cd $DEV_HOME/OSC
echo "Compiling OSC Python Scripts"
echo "===================================="
python -m compileall OSCServer.py 
echo
echo "Copying OSC files to $RELEASE_DIR" 
echo "===================================="
sudo cp -r $DEV_HOME/OSC/OSCServer.pyc $RELEASE_DIR/OSC
dos2unix -q $RELEASE_DIR/OSC/*
sudo chmod +x $RELEASE_DIR/OSC/*

#Do rangeSensor stuff
cd $DEV_HOME/rangeSensor
echo
echo "Compiling rangeSensor Python Scripts"
echo "===================================="
python -m compileall .
echo
echo "Copying rangeSensor Python Scripts to $RELEASE_DIR" 
echo "===================================="
sudo cp -R $DEV_HOME/rangeSensor/*.pyc $RELEASE_DIR/rangeSensor
sudo chmod +x $RELEASE_DIR/rangeSensor/*.pyc

#Copy Scripts
echo
echo "Copying init scripts to $RELEASE_DIR" 
echo "===================================="
sudo cp $DEV_HOME/scripts/init/* $RELEASE_DIR/scripts
dos2unix -q $RELEASE_DIR/scripts/init/*