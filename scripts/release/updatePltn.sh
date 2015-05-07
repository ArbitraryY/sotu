#!/bin/bash

DATE=`date +%Y-%m-%d-%T`
OPT=$1

if [ $# != 1 ]
then
	echo "usa`ge: $0 (push|pull)"
	echo "    push - /usr/local/pltn to pltn.git"
	echo "    pull - from pltn.git to /usr/local/pltn" 
	exit
fi

cd /usr/local/pltn

if [ $OPT == "push" ]
then 

	echo "-------- Staging Changes -------------------"
	echo " "
	git add *
	git add -u *

	echo "-------- Commiting to Git Repository -------------------"
	echo " "
	git commit -m "Updating pltn repository on ${DATE}"

	echo "-------- Push changes to Master -------------------"
	echo " "
	git push

	echo "Updated PLTN production repository on ${DATE}"
elif [ $OPT == "pull" ]
then
	echo "------- Updating pltn to latest version ----------"
	git pull
	
else
	echo "$OPT is not a valid option"
	exit
fi