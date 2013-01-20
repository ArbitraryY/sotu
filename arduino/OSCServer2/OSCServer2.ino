#include <SPI.h>
#include <Ethernet.h>

#include <ArdOSC.h>

int redPin = 5;
int greenPin = 6;
int bluePin = 3;

byte serverMac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
byte serverIp[]  = { 192, 168, 1, 17 };
int  serverPort  = 9999; //OSCserver listening port

OSCServer server;
OSCMessage *_mes;

void setup(){ 
  
 Serial.begin(19200);
 
 Ethernet.begin(serverMac ,serverIp); 
 server.begin(serverPort);
 
 //set callback function
 server.addCallback("/ard/led/red",&red);//turn a color on 
 //server.addCallback("/ard/led/green",&green);//turn a color off 
 //server.addCallback("/ard/led/blue",&blue);//turn a color off
 //server.addCallback("/ard/led/prog",&prog);//turn a color on 
 //all pins off
 analogWrite(redPin,0);
 analogWrite(greenPin,0);
 analogWrite(bluePin,0);
}
  
void loop(){
  if(server.aviableCheck()>0){
    Serial.println("alive! ");
  }
}

void red(OSCMessage *mes){
  int t;
  //get 1st argument(int32)
  t = mes->getArgInt32(0);
  Serial.println(t);
  
}
void colorOff(OSCMessage *mes){
  int t;
  //get 1st argument(int32)
  t = _mes->getArgInt32(0);
  Serial.println("ColorOff" + t);
}

void logOscAddress(OSCMessage *mes){
  Serial.println(mes->getOSCAddress());
} 
