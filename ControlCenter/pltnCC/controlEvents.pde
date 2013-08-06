public void controlEvent(ControlEvent c) {
  //find where the control event is coming from
  if (c.getName() == "picker"){
    //OscBundle myBundle = new OscBundle();
    int r = int(c.getArrayValue(0));
    int g = int(c.getArrayValue(1));
    int b = int(c.getArrayValue(2));
    int pickId = c.getId();
    //int a = int(c.getArrayValue(3));
    //color col = color(r,g,b,a);
    //get the ID of the color picker
    println(c.getName() + pickId);
    
    //Construct the red LED message
    sendOscMsg[pickId].setAddrPattern("/pltn/led");
    sendOscMsg[pickId].add("r1");
    sendOscMsg[pickId].add(r);
    sendOscMsg[pickId].add("solid");
    ccOscServer.send(sendOscMsg[pickId],oscRpi[pickId]);
    sendOscMsg[pickId].clear();
    sendOscMsg[pickId].setAddrPattern("/pltn/led");
    sendOscMsg[pickId].add("r2");
    sendOscMsg[pickId].add(r);
    sendOscMsg[pickId].add("solid");
    ccOscServer.send(sendOscMsg[pickId],oscRpi[pickId]);
    sendOscMsg[pickId].clear();
    //Construct the green LED message
    sendOscMsg[pickId].setAddrPattern("/pltn/led");
    sendOscMsg[pickId].add("g1");
    sendOscMsg[pickId].add(g);
    sendOscMsg[pickId].add("solid");
    //send to RPi OSC server
    ccOscServer.send(sendOscMsg[pickId],oscRpi[pickId]);
    sendOscMsg[pickId].clear();
    sendOscMsg[pickId].setAddrPattern("/pltn/led");
    sendOscMsg[pickId].add("g2");
    sendOscMsg[pickId].add(g);
    sendOscMsg[pickId].add("solid");
    //send to RPi OSC server
    ccOscServer.send(sendOscMsg[pickId],oscRpi[pickId]);
    sendOscMsg[pickId].clear();
    //Construct the blue LED message
    sendOscMsg[pickId].setAddrPattern("/pltn/led");
    sendOscMsg[pickId].add("b1");
    sendOscMsg[pickId].add(b);
    sendOscMsg[pickId].add("solid");
    //send to RPi OSC server
    ccOscServer.send(sendOscMsg[pickId],oscRpi[pickId]);
    sendOscMsg[pickId].clear();
    sendOscMsg[pickId].setAddrPattern("/pltn/led");
    sendOscMsg[pickId].add("b2");
    sendOscMsg[pickId].add(b);
    sendOscMsg[pickId].add("solid");
    //send to RPi OSC server
    ccOscServer.send(sendOscMsg[pickId],oscRpi[pickId]);
    sendOscMsg[pickId].clear();
    println("event\tred:"+r+"\tgreen:"+g+"\tblue:"+b);
  }
  else if (c.getName() == "shutdown"){
    println(c.getId());
    //get the id of the button that was pressed
    int shutdownId = c.getId();
    //construct the shutdown message
    sendOscMsg[shutdownId].setAddrPattern("/pltn/rpi");
    sendOscMsg[shutdownId].add("off");
    sendOscMsg[shutdownId].add(rpiAuthKey);
    println(rpiAuthKey);
    //Send thee shutdown message
    ccOscServer.send(sendOscMsg[shutdownId],oscRpi[shutdownId]);
    sendOscMsg[shutdownId].clear();
  }
  else {
    //not a monitored control event
  }
}
