// OSCClass simple recieve test Arduino sketch
// OSCClass version 1.0.1 (Arduino ver0014)
// Copyright (c) recotana(http://recotana.com).  All right reserved.

#include "Ethernet.h"
#include "OSCClass.h"
#include "SPI.h"

  byte serverMac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
  byte serverIp[]  = { 192, 168, 1, 177 };
  int  serverPort  = 9999;
  
//  byte gateway[]   = { 192, 168, 0, 1 };
//  byte subnet[]    = { 255, 255, 255, 0 };


  byte destIp[]  = { 192, 168, 0, 5};
  int  destPort = 10000;
  
  char *topAddress="/ard";
  char *subAddress[3]={ "/test1" , "/test2" , "/test3" };
  
  OSCMessage recMes;
  
  OSCClass osc(&recMes);

void setup() {
  
     Ethernet.begin(serverMac ,serverIp);
 //    Ethernet.begin(serverMac ,serverIp ,gateway ,subnet);
    
     //setting osc recieve server
     osc.begin(serverPort);
   
   
     //for message logging
     Serial.begin(19200);
     
     //osc message buffer clear
     osc.flush();
     
     
}

void loop() {

    //osc arrive check
    if ( osc.available() ) {
      
        logMessage(&recMes);

    }

}




// *********  utility  ***********************************


void logMessage(OSCMessage *mes){
  
    uint8_t *ip=mes->getIp();
  
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
    for(int i = 0 ; i < mes->getAddressNum() ; i++){
      
      Serial.print(mes->getAddress(i));
      
    }
    
    
    //disp type tags
    Serial.print("  ,");
    for(int i = 0 ; i < mes->getArgNum() ; i++){
      
      Serial.print(mes->getTypeTag(i));
      
    }
    Serial.print(" ");
   
   
   //disp args
    for(int i = 0 ; i < mes->getArgNum() ; i++){
      
      switch( mes->getTypeTag(i) ){
        
        case 'i': {
                      
                      Serial.print( mes->getArgInt(i) );
                  }
          break;
        
        case 'f':  {
                      
                      Serial.print( mes->getArgFloat(i) );
                  }
          break;
         
      }
      
       Serial.print(" ");
      
    }
    
    Serial.println(""); 
    
}
