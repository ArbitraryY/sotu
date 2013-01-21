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
 server.addCallback("/ard/red",&red); 
 server.addCallback("/ard/green",&green); 
 server.addCallback("/ard/blue",&blue);
 server.addCallback("/ard/player",&player);
 server.addCallback("/ard/prog",&prog); 
 //all pins off
 analogWrite(redPin,0);
 analogWrite(greenPin,0);
 analogWrite(bluePin,0);
}
  
void loop(){
  if(server.aviableCheck()>0){
  //  Serial.println("alive! ");
  }
}

void red(OSCMessage *mes){
  int rVal = (int) mes->getArgFloat(0);
  analogWrite(redPin,rVal);
}

void green(OSCMessage *mes){
  int gVal = (int) mes->getArgFloat(0);
  analogWrite(greenPin,gVal);
}

void blue(OSCMessage *mes){
  int bVal = (int) mes->getArgFloat(0);
  analogWrite(bluePin,bVal);
}

void player(OSCMessage *mes){
  //int val=(int) mes->getArgFloat(0);
  int val=mes->getArgInt32(0);
  Serial.println(val);
  if(val == 1) {
    analogWrite(redPin,255);
    analogWrite(greenPin,0);
    analogWrite(bluePin,0);
  } else if(val == 2) {
    analogWrite(redPin,0);
    analogWrite(greenPin,255);
    analogWrite(bluePin,0);
  } else if(val == 3) {
    analogWrite(redPin,0);
    analogWrite(greenPin,0);
    analogWrite(bluePin,255);
  } else {
    analogWrite(redPin,0);
    analogWrite(greenPin,0);
    analogWrite(bluePin,0);
  }
}

void prog(OSCMessage *mes){
  
}
