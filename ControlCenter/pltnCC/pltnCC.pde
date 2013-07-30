import controlP5.*;
import oscP5.*;
import netP5.*;

int numPis = 6;
ControlP5[] cp5 = new ControlP5[numPis];
ColorPicker[] cPick = new ColorPicker[numPis];
Textlabel[] hostname = new Textlabel[numPis];
DrawRegions[] region = new DrawRegions[numPis];
PltnHosts pHosts = new PltnHosts();
NetAddress[] oscRpi = new NetAddress[numPis];
OscP5 ccOscServer;

void setup() {
  //Size of the window
  size(1020, 400);
  //create all objects used
  createObjs();
  //draw the CC layout 
  drawLayout();
  
  //OSC Stuff
  ccOscServer = new OscP5(this,12000); //listens on port 12000
  //OSC Callback Definitions ("OSC Plugs")
  //args (object,callback function name, Received OSC address) 
  ccOscServer.plug(this,"printme","/test");
  frameRate(25);
 }

void draw() {
  //background(cPick1.getColorValue());
}

void oscEvent(OscMessage theOscMessage) {
  /* print the address pattern and the typetag of the received OscMessage */
  print("### received an osc message.");
  print(" addrpattern: "+theOscMessage.addrPattern());
  println(" typetag: "+theOscMessage.get(0).intValue());
  
 if(theOscMessage.isPlugged()==false) {
   /* print the address pattern and the typetag of the received OscMessage */
   println("### received an osc message.");
   println("### addrpattern\t"+theOscMessage.addrPattern());
   println("### typetag\t"+theOscMessage.typetag());
 }
}
