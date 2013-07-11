#!/usr/bin/python

from os import system

CORE_RELEASE_DIR    = "/usr/local/pltn"
MODULES_RELEASE_DIR = CORE_RELEASE_DIR+"/Modules"
DEV_HOME            = "/home/pltn/platoon"
MODULES_DIR         = DEV_HOME+"/Modules"
WEBAPP_DIR          = DEV_HOME+"/webapp"
INIT_SCRIPTS_DIR    = DEV_HOME+"/scripts/init"

#core pltn files
core_dirs   = ["pltnAgent", "OSC", "rangeSensor"]
#PLTN modules
module_dirs = ["LED","GPIO","Pblstr","rsDistance"]
#Other dirs to copy
other_dirs  = ["webapp","scripts"]

#compile and release core PLTN scripts
for dir in core_dirs:
    srcDir = DEV_HOME+"/"+dir
    print "Compiling: "+srcDir
    compileCmd = "python -m compileall "+srcDir
    system(compileCmd)
    rsyncCmd = "sudo rsync -r --exclude=*.py "+srcDir+" "+CORE_RELEASE_DIR
    system(rsyncCmd)
    print "\n"
    print "--------------------------------------"

#Compile and release PLTN modules
for dir in module_dirs:
    srcDir = MODULES_DIR+"/"+dir
    print "Compiling: "+srcDir
    compileCmd = "python -m compileall "+srcDir
    system(compileCmd)
    rsyncCmd = "sudo rsync -r --exclude=*.py "+srcDir+" "+MODULES_RELEASE_DIR
    system(rsyncCmd)
    print "\n"
    print "--------------------------------------"

#Copy other webapp
print "Releasing webapp"
webRsyncCmd = "rsync -r --exclude=archive "+WEBAPP_DIR+"/* "+CORE_RELEASE_DIR+"/webapp"
system(webRsyncCmd)

initRsyncCmd = "rsync -r "+INIT_SCRIPTS_DIR+"/* "+CORE_RELEASE_DIR+"/scripts"
system(initRsyncCmd)
    
d2uCmd = "dos2unix -q -R "+CORE_RELEASE_DIR
system(d2uCmd)
chmodCmd = "sudo chmod -R +x "+CORE_RELEASE_DIR 
system(chmodCmd)   