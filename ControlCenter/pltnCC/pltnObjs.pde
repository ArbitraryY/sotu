//Textlabel hostname;

//create ControlP5 objects
void createObjs(){
  for (int i=0 ; i < numPis ; i++) {
    cp5[i]    = new ControlP5(this);
    region[i] = new DrawRegions();
    //oscServer[] = new OscP5(this,12000);//the local port to listen on
    //oscRpi[] = new NetAddress(pHosts.getIp("PLTN"+str(i+1)),);//remote RPi IP and port
  } 
}
