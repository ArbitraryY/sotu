#include "Ethernet.h"
#include "OSCClass.h"
#include "SPI.h"

int redPin = 5;
int greenPin = 6;
int bluePin = 3;

  byte serverMac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
  byte serverIp[]  = { 192, 168, 1, 17 };
  int  serverPort  = 9999;
  
//  byte gateway[]   = { 192, 168, 0, 1 };
//  byte subnet[]    = { 255, 255, 255, 0 };
// byte destIp[]  = { 192, 168, 0, 5};
// int  destPort = 10000;
  
  //char *topAddress="/ard";
  //char *subAddress[3]={ "/redPin" , "/greenPin" , "/bluePin" };
  //char *subAddress[3]={ "/test1" , "/test2" , "/test3" };
  //char *subAddress[1]={ "/pin"};
  
  OSCMessage recMes;
  
  OSCClass osc(&recMes);

void setup() {
  
     Ethernet.begin(serverMac ,serverIp);
     //setting osc recieve server
     osc.begin(serverPort);
     //for message logging
     Serial.begin(19200);
     //osc message buffer clear
     osc.flush();
     //
     analogWrite(redPin,0);
     analogWrite(greenPin,0);
     analogWrite(bluePin,0);
}

void loop() {
    //osc arrive check
    //analogWrite(redPin,255);
    if ( osc.available() ) {
       logMessage(&recMes);
    }
}
// *********  utility  ***********************************


void logMessage(OSCMessage *mes){
  
    uint8_t *ip=mes->getIp();
    
    //Serial.println(mes->getAddress(1));
     //disp ip & port
    Serial.print("from IP:");
    Serial.print(ip[0],DEC);
    Serial.print(".");
    Serial.print(ip[1],DEC);
    Serial.print(".");
    Serial.print(ip[2],DEC);
    Serial.print(".");
    Serial.print(ip[3],DEC);
    Serial.print(" port:");
    Serial.print(mes->getPort(),DEC);
    Serial.print("   ");
    
   //disp adr
   /*for(int i = 0 ; i < mes->getAddressNum() ; i++){
    Serial.print(mes->getAddress(i));
   }*/
   
   //disp type tags
   
   //debug
   /*for(int i = 0 ; i < mes->getArgNum() ; i++){
     Serial.print(mes->getTypeTag(i));
     Serial.print(mes->getArgInt(i));
     Serial.print(mes->getArgNum());
     Serial.print(subAddress[i]);
     
   //}*/
     Serial.print(", ");
     Serial.print("SubAddr: ");
     Serial.print( mes->getSubAddress()[0] );//first char in array
     Serial.print( mes->getSubAddress()[1] );//second char in array
     Serial.print(" Value: ");
     Serial.print( mes->getArgInt(0) );//first value
     // check if subAddress sent:
     // (r)ed (g)reen (b)lue (r)ed(S)lider (s)equence
     if ( mes->getSubAddress()[0] == 'r' ) {
       analogWrite(redPin,mes->getArgInt(0));
     } 
     else if ( mes->getSubAddress()[0] == 'g' ) {
       analogWrite(greenPin,mes->getArgInt(0));
     } 
     else if ( mes->getSubAddress()[0] == 'b' ) {
       analogWrite(bluePin,mes->getArgInt(0));
     } 
     else if ( mes->getSubAddress()[0] == 'r' && mes->getSubAddress()[1] == 'S' ) {
       analogWrite(redPin,mes->getArgInt(0));
   } else if ( mes->getSubAddress()[0] == 's' ) {//Processing MP3 Player
       if(mes->getArgInt(0) == 1) {
         analogWrite(redPin,255);
         analogWrite(greenPin,0);
         analogWrite(bluePin,0);
       } else if(mes->getArgInt(0) == 2) {
         analogWrite(redPin,0);
         analogWrite(greenPin,255);
         analogWrite(bluePin,0);
       } else if(mes->getArgInt(0) == 3) {
         analogWrite(redPin,0);
         analogWrite(greenPin,0);
         analogWrite(bluePin,255);
       } else if(mes->getArgInt(0) == 4) {//Fade between colors
         FadeRGB(mes);
       } else if (mes->getArgInt(0) == 5){ 
         void(* resetFunc) (void) = 0;
         resetFunc();
       } else if(mes->getArgInt(0) == 6) {//All on
           analogWrite(redPin,255);
           analogWrite(greenPin,255);
           analogWrite(bluePin,255);
       } else {//Off
           analogWrite(redPin,0);
           analogWrite(greenPin,0);
           analogWrite(bluePin,0);
       }
     } 
    Serial.println("");
    
} //End void Loop()

//RGB Fade Function
// OSC Message = /ard/s 4
void FadeRGB(OSCMessage *mes) {
  int i = 0;
  int fadeSpeed = 5;
  while (i == 0){
    int j = 0;
    for (j=0 ; j <=255 ; j++){
      analogWrite(redPin,j);
      analogWrite(greenPin,0);
      analogWrite(bluePin,0);
      delay(fadeSpeed);
    }
    for (j=0 ; j <=255 ; j++){
      analogWrite(redPin,0);
      analogWrite(greenPin,j);
      analogWrite(bluePin,0);
      delay(fadeSpeed);
    }
    for (j=0 ; j <=255 ; j++){
      analogWrite(redPin,0);
      analogWrite(greenPin,0);
      analogWrite(bluePin,j);
      delay(fadeSpeed);
    }
  }
}
