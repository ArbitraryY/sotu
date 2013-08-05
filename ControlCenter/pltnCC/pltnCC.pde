import controlP5.*;
import oscP5.*;
import netP5.*;

int numPis = 2;
ControlP5[] cp5 = new ControlP5[numPis];
ColorPicker[] cPick = new ColorPicker[numPis];
Textlabel[] hostname = new Textlabel[numPis];
DrawRegions[] region = new DrawRegions[numPis];
PltnHosts pHosts = new PltnHosts();
NetAddress[] oscRpi = new NetAddress[numPis];
OscP5 ccOscServer;

void setup() {
   background(#000000);
  //Size of the window
  size(400, 350);
  //create all objects used
  createObjs();
  //draw the CC layout 
  drawLayout();
  
  //OSC Stuff
  ccOscServer = new OscP5(this,12000); //listens on port 12000
  //OSC Callback Definitions ("OSC Plugs")
  //args (object,callback function name, Received OSC address) 
  ccOscServer.plug(this,"heartBeat","/pltn/heartbeat");
  frameRate(25);
 }

void draw() {
  //background(cPick1.getColorValue());
}

void oscEvent(OscMessage theOscMessage) {
  /* print the address pattern and the typetag of the received OscMessage */
  fill(0);
  String mesg = "hello";
  text(mesg,50,150);
  print("### received an osc message.");
  print(" addrpattern: "+theOscMessage.addrPattern());
  println(" value: "+theOscMessage.get(0).intValue());
  
 if(theOscMessage.isPlugged()==false) {
   /* print the address pattern and the typetag of the received OscMessage */
   println("### received an osc message.");
   println("### addrpattern\t"+theOscMessage.addrPattern());
   println("### typetag\t"+theOscMessage.typetag());
 }
}
