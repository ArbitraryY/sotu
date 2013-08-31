//These functions are the OSC Callback functions for the messages received
public void heartBeat(String host, String srvc, int status){
  //This function will populate the layout with the values reported from the RPis
  fill(255);
  //text(srvc+": "+status ,15,250);
 // switch(
  //rectangle()
  println(host+ ": " + srvc+ " " +status);
}
