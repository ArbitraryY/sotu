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
 server.addCallback("/ard/red",&red);//turn a color on 
 server.addCallback("/ard/green",&green);//turn a color off 
 server.addCallback("/ard/blue",&blue);//turn a color off
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
  int rVal = (int) mes->getArgFloat(0);
  analogWrite(redPin,rVal);
  Serial.println(rVal);
  Serial.println(mes->getOSCAddress());
}

void green(OSCMessage *mes){
  int gVal = (int) mes->getArgFloat(0);
  analogWrite(greenPin,gVal);
  //debug
  Serial.println(gVal);
  Serial.println(mes->getOSCAddress());
}

void blue(OSCMessage *mes){
  int bVal = (int) mes->getArgFloat(0);
  analogWrite(bluePin,bVal);
  //debug
  Serial.println(bVal);
  Serial.println(mes->getOSCAddress());
}
