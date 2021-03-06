public void controlEvent(ControlEvent c) {
  //find where the control event is coming from
  if (c.getName() == "picker"){
    //scale values down for pi-blaster needs 0 - 1
    float r = c.getArrayValue(0)/255.0;
    float g = c.getArrayValue(1)/255.0;
    float b = c.getArrayValue(2)/255.0;
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
    //Send the shutdown message
    ccOscServer.send(sendOscMsg[shutdownId],oscRpi[shutdownId]);
    sendOscMsg[shutdownId].clear();
  } else if (c.getName() == "allOff"){
    println(c.getId());
    //get the id of the button that was pressed
    int id = c.getId();
    sendOscMsg[id].setAddrPattern("/pltn/led");
    sendOscMsg[id].add("allOff");
    //Send the message
    ccOscServer.send(sendOscMsg[id],oscRpi[id]);
    sendOscMsg[id].clear();
  } else if (c.getName() == "allOn"){
    println(c.getId());
    //get the id of the button that was pressed
    int id = c.getId();
    sendOscMsg[id].setAddrPattern("/pltn/led");
    sendOscMsg[id].add("allOn");
    //Send the message
    ccOscServer.send(sendOscMsg[id],oscRpi[id]);
    sendOscMsg[id].clear();
  }
  else {
    //not a monitored control event
  }
}
