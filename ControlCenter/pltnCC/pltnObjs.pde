//Textlabel hostname;

//create ControlP5 objects
void createObjs(){
  for (int i=0 ; i < numPis ; i++) {
    cp5[i]    = new ControlP5(this);
    //region[i] = new DrawRegions();
    //OSC server objects for each RPi
    oscRpi[i] = new NetAddress(pHosts.getIp("PLTN"+str(i+1)),rpiOscServerPort);//remote RPi IP and port
    sendOscMsg[i] = new OscMessage("");
  } 
}
