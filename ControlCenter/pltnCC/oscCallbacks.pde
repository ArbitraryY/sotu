//These functions are the OSC Callback functions for the messages received
public void heartBeat(String host, String service, int status, int pid){
  //This function will populate the layout with the values reported from the RPis
  fill(255);
  text(service+ " " + status+ " " +pid ,30,400);
}
