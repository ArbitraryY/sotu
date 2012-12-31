import ddf.minim.*;
import ddf.minim.analysis.*;
import processing.serial.*;
import cc.arduino.*;

Minim minim;
AudioPlayer song;
BeatDetect beat;
BeatListener bl;
Arduino arduino;
int redPin = 11;
int greenPin = 12;
int bluePin = 13;
int redOutput = 1;
int greenOutput = 2;
int blueOutput = 3;
String rVal;
String gVal;
String bVal;

void setup()
{
  size(512, 200, P3D);
  //println(Arduino.list());
  arduino = new Arduino(this, Arduino.list()[0], 57600);
  arduino.pinMode(redPin, Arduino.OUTPUT);
  arduino.pinMode(greenPin, Arduino.OUTPUT);
  arduino.pinMode(bluePin, Arduino.OUTPUT);
  //set pins to input mode for debugging
  arduino.pinMode(redOutput, Arduino.INPUT);
  arduino.pinMode(greenOutput, Arduino.INPUT);
  arduino.pinMode(blueOutput, Arduino.INPUT);
   
  minim = new Minim(this);
  
  //song = minim.loadFile("C:\\Users\\nick\\Documents\\Processing\\audio_test\\data\\questionMarksAndOtherDemonicPunctuation.mp3", 2048);
  song = minim.loadFile("C:\\Users\\nick\\Documents\\Processing\\audio_test\\data\\aSummersDream.mp3", 2048);
  song.play();
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
  beat.setSensitivity(100);  
  // make a new beat listener, so that we won't miss any buffers for the analysis
  bl = new BeatListener(beat, song);
}

void draw()
{
  background(0);
  fill(255);
  if ( beat.isKick() ) {
    arduino.digitalWrite(redPin, Arduino.LOW);
    arduino.digitalWrite(bluePin, Arduino.HIGH);
    arduino.digitalWrite(greenPin, Arduino.HIGH);
    println("kick");
    arduino.digitalWrite(redOutput, Arduino.LOW);
    arduino.digitalWrite(greenOutput, Arduino.HIGH);
    arduino.digitalWrite(blueOutput, Arduino.HIGH);
  }
  else if ( beat.isSnare() ) {
    arduino.digitalWrite(redPin, Arduino.HIGH);
    arduino.digitalWrite(bluePin, Arduino.LOW);
    arduino.digitalWrite(greenPin, Arduino.HIGH);
    println("snare");
    arduino.digitalWrite(redOutput, Arduino.HIGH);
    arduino.digitalWrite(greenOutput, Arduino.LOW);
    arduino.digitalWrite(blueOutput, Arduino.HIGH);
  }
  else if ( beat.isHat() ) {
    arduino.digitalWrite(redPin, Arduino.HIGH);
    arduino.digitalWrite(bluePin, Arduino.HIGH);
    arduino.digitalWrite(greenPin, Arduino.LOW);
    
    arduino.digitalWrite(redOutput, Arduino.HIGH);
    arduino.digitalWrite(greenOutput, Arduino.HIGH);
    arduino.digitalWrite(blueOutput, Arduino.LOW);
    println("hat");
  } else {
    arduino.digitalWrite(redPin, Arduino.HIGH);
    arduino.digitalWrite(bluePin, Arduino.HIGH);
    arduino.digitalWrite(greenPin, Arduino.HIGH);
    
    arduino.digitalWrite(redOutput, Arduino.HIGH);
    arduino.digitalWrite(greenOutput, Arduino.HIGH);
    arduino.digitalWrite(blueOutput, Arduino.HIGH);
  }
 println("--------------");
 if (arduino.digitalRead(redOutput) == Arduino.HIGH){
   println("HIGH");
 } else if (arduino.digitalRead(redOutput) == Arduino.LOW){
   println("LOW");
 }
  if (arduino.digitalRead(greenOutput) == Arduino.HIGH){
   println("HIGH");
 } else if (arduino.digitalRead(greenOutput) == Arduino.LOW){
   println("LOW");
 }
  if (arduino.digitalRead(blueOutput) == Arduino.HIGH){
   println("HIGH");
 } else if (arduino.digitalRead(blueOutput) == Arduino.LOW){
   println("LOW");
 }
 println(arduino.analogRead(redOutput));
 println(arduino.analogRead(greenOutput));
 println(arduino.analogRead(blueOutput));
 println("--------------");
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

