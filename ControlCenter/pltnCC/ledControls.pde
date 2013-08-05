public void controlEvent(ControlEvent c) {
  //find where the control event is coming from
  if(c.isFrom(cPick[0]) || c.isFrom(cPick[1])) {
    int r = int(c.getArrayValue(0));
    int g = int(c.getArrayValue(1));
    int b = int(c.getArrayValue(2));
    //int a = int(c.getArrayValue(3));
    //color col = color(r,g,b,a);
    //Construct the LED message
    sendOscMsg[0] = new OscMessage("/pltn/led");
    sendOscMsg[0].add("test");
    //send to RPi OSC server
    ccOscServer.send(sendOscMsg[0],oscRpi[0]);
    println("event\tred:"+r+"\tgreen:"+g+"\tblue:"+b);
  }
}
