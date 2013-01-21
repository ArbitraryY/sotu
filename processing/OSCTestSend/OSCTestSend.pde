import oscP5.*;
import netP5.*;

OscP5 oscP5;
NetAddress arduinoAddress;

int flag = 0;

void setup(){
  size(67, 50);
  frameRate(25);
  oscP5 = new OscP5(this,10000);
  arduinoAddress = new NetAddress("192.168.1.17",9999);
}

void draw (){
  OscMessage pinMsg = new OscMessage("/ard/red");
  if (flag == 0) {
    pinMsg.add(255.0);
    flag = 1;
  } else {
    pinMsg.add(0.0);
    flag = 0;
  }
  println(pinMsg.addrPattern());
  println("----------------");
  oscP5.send(pinMsg, arduinoAddress);
}
