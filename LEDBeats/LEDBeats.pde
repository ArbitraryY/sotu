import ddf.minim.*;
import ddf.minim.analysis.*;
import processing.serial.*;
import cc.arduino.*;
import oscP5.*;
import netP5.*;

OscP5 oscP5;
NetAddress arduinoAddress;
Minim minim;
AudioPlayer song;
BeatDetect beat;
BeatListener bl;
Arduino arduino;
//for serial only
//int redPin = 5;
//int greenPin = 6;
//int bluePin = 3;

void setup()
{
  size(500, 500, P3D);
  /*println(Arduino.list());
  arduino = new Arduino(this, Arduino.list()[0], 57600);
  arduino.pinMode(redPin, Arduino.OUTPUT);
  arduino.pinMode(greenPin, Arduino.OUTPUT);
  arduino.pinMode(bluePin, Arduino.OUTPUT);
  //start with all off
  arduino.analogWrite(redPin, 0);
  arduino.analogWrite(greenPin, 0);
  arduino.analogWrite(bluePin, 0);*/
  
  minim = new Minim(this); 
  
  //song = minim.loadFile("C:\\Users\\nick\\Documents\\Processing\\audio_test\\data\\questionMarksAndOtherDemonicPunctuation.mp3", 2048);
  song = minim.loadFile("C:\\Users\\nick\\Documents\\Processing\\audio_test\\data\\aSummersDream.mp3", 2048);
  // a beat detection object that is FREQ_ENERGY mode that 
  // expects buffers the length of song's buffer size
  // and samples captured at songs's sample rate
  beat = new BeatDetect(song.bufferSize(), song.sampleRate());
  // set the sensitivity to 300 milliseconds
  // After a beat has been detected, the algorithm will wait for 300 milliseconds 
  // before allowing another beat to be reported. You can use this to dampen the 
  // algorithm if it is giving too many false-positives. The default value is 10, 
  // which is essentially no damping. If you try to set the sensitivity to a negative value, 
  // an error will be reported and it will be set to 10 instead. 
  beat.setSensitivity(300);  
  // make a new beat listener, so that we won't miss any buffers for the analysis
  bl = new BeatListener(beat, song);
  
  oscP5 = new OscP5(this,10000);
  arduinoAddress = new NetAddress("192.168.1.177",9999);
}

void draw()
{
  background(0);
  fill(255);
  fill(255,0,0);
  rect(30, 30, 50, 50);
  textSize(16);
  fill(0,0,0);
  text("play",40,55);
  
  OscMessage pinMsg = new OscMessage("/ard/s");
  if ( beat.isKick() ) {
    println("kick");
    fill(255,0,0);
    rect(50,200,400,200);
   //send OSC message - send 1 to activate red LED
    pinMsg.add(1);
    //Serial write
    //arduino.analogWrite(redPin, 255);
    //arduino.analogWrite(bluePin, 0);
    //arduino.analogWrite(greenPin, 0);
  }
  else if ( beat.isSnare() ) {
    println("snare");
    fill(0,255,0);
    rect(50,200,400,200);
    //send OSC message - send 2 to activate green LED
    pinMsg.add(2);    
    //Serial write
    //arduino.analogWrite(redPin, 0);
    //arduino.analogWrite(greenPin, 255);
    //arduino.analogWrite(bluePin, 0);
  }
  else if ( beat.isHat() ) {
    println("hat");
    fill(0,0,255);
    rect(50,200,400,200);
    //send OSC message - send 3 to activate blue LED
    pinMsg.add(3);
    //Serial write
    //arduino.analogWrite(redPin, 0);
    //arduino.analogWrite(greenPin, 0);
    //arduino.analogWrite(bluePin, 255);
  } else {
   //send OSC message - all Off
    pinMsg.add(4);
    //Serial write
    //arduino.analogWrite(redPin, 0);
    //arduino.analogWrite(bluePin, 0);
    //arduino.analogWrite(greenPin, 0);
  }
  //send the OSC message to arduino
  oscP5.send(pinMsg, arduinoAddress);

}

void mousePressed() {
  if(mouseX>30 && mouseX<80) //co-ordinates for button area
    if(mouseY>30 && mouseY<80)
      if (song.isPlaying()){  //button function, ie play/pause
        song.pause();
      }
    else{
      song.play();
    }

}

void stop()
{
  // always close Minim audio classes when you are finished with them
  song.close();
  // always stop Minim before exiting
  minim.stop();
  // this closes the sketch
  super.stop();
}

