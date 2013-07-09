#!/bin/bash

RELEASE_DIR=/usr/local/pltn
DEV_HOME=/home/pltn/platoon

#Copy and Compile Agent
cd $DEV_HOME/pltnAgent
echo "Compiling Agent Python Scripts"
echo "===================================="
python -m compileall . 
echo
echo "Copying Agent files to $RELEASE_DIR" 
echo "===================================="
sudo rsync -rv $DEV_HOME/pltnAgent/*.pyc $RELEASE_DIR/pltnAgent

#Copy OSC related files
cd $DEV_HOME/OSC
echo "Compiling OSC Python Scripts"
echo "===================================="
python -m compileall OSCServer.py 
echo
echo "Copying OSC files to $RELEASE_DIR" 
echo "===================================="
sudo rsync -rv $DEV_HOME/OSC/OSCServer.pyc $RELEASE_DIR/OSC

#Do rangeSensor stuff
cd $DEV_HOME/rangeSensor
echo
echo "Compiling rangeSensor Python Scripts"
echo "===================================="
python -m compileall .
echo
echo "Copying rangeSensor Python Scripts to $RELEASE_DIR" 
echo "===================================="
sudo rsync -rv $DEV_HOME/rangeSensor/*.pyc $RELEASE_DIR/rangeSensor

#Copy Scripts
echo
echo "Copying init scripts to $RELEASE_DIR" 
echo "===================================="
sudo rsync -rv $DEV_HOME/scripts/init/* $RELEASE_DIR/scripts

#Copy Web App
echo
echo "Copying web application to $RELEASE_DIR"
echo "========================================"
sudo rsync -rv --exclude=archive $DEV_HOME/webapp/* $RELEASE_DIR/webapp

#Change all scripts to UNIX format and update to execute permissions
echo
echo "Updating Permissions"
echo "===================================="
dos2unix -q -R $RELEASE_DIR/*
sudo chmod -R +x $RELEASE_DIR