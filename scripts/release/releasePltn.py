#!/usr/bin/python

from os import system

CORE_RELEASE_DIR    = "/usr/local/pltn"
MODULES_RELEASE_DIR = CORE_RELEASE_DIR+"/Modules"
DEV_HOME            = "/home/pltn/platoon"
MODULES_DIR         = DEV_HOME+"/Modules"
WEBAPP_DIR          = DEV_HOME+"/webapp"
INIT_SCRIPTS_DIR    = DEV_HOME+"/scripts/init"

#core pltn files to compile and copy to the release dir
core_dirs   = ["pltnAgent", "OSC", "rangeSensor"]
#PLTN modules to compile and copy to the release dir
module_dirs = ["LED","pltnGpio","Pblstr","rsDistance"]
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
    #Create directory if it doesn't exist
    mkDirCmd = "mkdir -p "+srcDir
    print mkDirCmd
    system(mkDirCmd)
    rsyncCmd = "sudo rsync -r --exclude=*.py "+srcDir+" "+MODULES_RELEASE_DIR
    print(rsyncCmd)
    system(rsyncCmd)
    print "\n"
    print "--------------------------------------"

#Copy other webapp
print "Releasing webapp"
webRsyncCmd = "rsync -r --exclude=archive "+WEBAPP_DIR+"/* "+CORE_RELEASE_DIR+"/webapp"
system(webRsyncCmd)

# Copying init scripts
initRsyncCmd = "rsync -r "+INIT_SCRIPTS_DIR+"/* "+CORE_RELEASE_DIR+"/scripts"
system(initRsyncCmd)

# Converting to Unix format
d2uCmd = "dos2unix -q -R "+CORE_RELEASE_DIR
system(d2uCmd)

# Updating permissions
chmodCmd = "sudo chmod -R +x "+CORE_RELEASE_DIR 
system(chmodCmd)   