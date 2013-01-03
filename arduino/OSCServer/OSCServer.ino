// OSCClass simple recieve test Arduino sketch
// OSCClass version 1.0.1 (Arduino ver0014)
// Copyright (c) recotana(http://recotana.com).  All right reserved.

#include "Ethernet.h"
#include "OSCClass.h"
#include "SPI.h"

int redPin = 5;
int greenPin = 6;
int bluePin = 3;

  byte serverMac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
  byte serverIp[]  = { 192, 168, 1, 177 };
  int  serverPort  = 9999;
  
//  byte gateway[]   = { 192, 168, 0, 1 };
//  byte subnet[]    = { 255, 255, 255, 0 };
// byte destIp[]  = { 192, 168, 0, 5};
// int  destPort = 10000;
  
  char *topAddress="/ard";
  char *subAddress[3]={ "/redPin" , "/greenPin" , "/bluePin" };
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
     Serial.print( mes->getArgInt(0) );//
     //getSubAddress is a character Array of length defined by the second address
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
       Serial.print("helloYes");
       analogWrite(bluePin,mes->getArgInt(0));
   }
   
   //disp args
   /*for(int i = 0 ; i < mes->getArgNum() ; i++){      
      switch( mes->getTypeTag(i) ){
        case 'i': {   
            if (i == 0) {//first element
              switch ( mes->getArgInt(0) ){
                case 1: //Red Only
                  analogWrite(redPin,mes->getArgInt(1));
                  analogWrite(greenPin,0);
                  analogWrite(bluePin,0);
                  break;
                case 2: //Green Only
                  analogWrite(redPin,0);
                  analogWrite(greenPin,255);
                  analogWrite(bluePin,0);
                  break;
                case 3: //Blue Only
                  analogWrite(redPin,0);
                  analogWrite(greenPin,0);
                  analogWrite(bluePin,255);
                  break;
                case 4: //Red On
                  analogWrite(redPin,255);
                  break;
                case 5: //Green On
                  analogWrite(greenPin,255);
                  break;
                case 6: //Blue On
                  analogWrite(bluePin,255);
                  break;
                case 7: //Red Off
                  analogWrite(redPin,0);
                  break;
                case 8: //Green Off
                  analogWrite(greenPin,0);
                  break;
                case 9: //Blue Off
                  analogWrite(bluePin,0);
                  break;
                case 10: //Red Slider
                  analogWrite(redPin,mes->getArgInt(1)*255);
                  break;
                case 100: //Off
                  analogWrite(redPin,0);
                  analogWrite(greenPin,0);
                  analogWrite(bluePin,0);
                  break;
                default: //Off
                  analogWrite(redPin,0);
                  analogWrite(greenPin,0);
                  analogWrite(bluePin,0);
                  break;
              }
           }
        }
        break;
        case 'f':  {      
                      Serial.print( mes->getArgFloat(i) );
                  }
          break;  
      }
       Serial.print(" "); 
    }*/
    Serial.println("");
    
} //End void Loop()
