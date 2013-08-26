import controlP5.*;
import oscP5.*;
import netP5.*;

int numPis = 3;//number of RPis
ControlP5[] cp5 = new ControlP5[numPis];
//Color picker objects
ColorPicker[] cPick = new ColorPicker[numPis];
Textlabel[] hostname = new Textlabel[numPis];
PltnHosts pHosts = new PltnHosts();
//OSC Server location objects
NetAddress[] oscRpi = new NetAddress[numPis];
//OSC message objects
OscMessage[] sendOscMsg = new OscMessage[numPis];
//Local OSC Server object
OscP5 ccOscServer;

void setup() {
   background(#000000);
  //Size of the window
  size(numPis*165, 350);
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
  print("### received an osc message.");
  print(" addrpattern: "+theOscMessage.addrPattern());
  println(" value: "+theOscMessage.get(0).stringValue());
  fill(255);
  //text(theOscMessage.get(0).stringValue(),30,325);
  
 if(theOscMessage.isPlugged()==false) {
  // print the address pattern and the typetag of the received OscMessage
   println("### received an osc message.");
   println("### addrpattern\t"+theOscMessage.addrPattern());
   println("### typetag\t"+theOscMessage.typetag());
 }
}
