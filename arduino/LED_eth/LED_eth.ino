const float pi = 3.14;

//LED pinouts
int redPin = 3; 
int greenPin = 5; 
int bluePin = 6;
int brightness = 0;    // how bright the LED is
int fadeAmount = 5;    // how many points to fade the LED by
int xStep = 0;
int radStep = pi/4; //step amount in radians

// the setup routine runs once when you press reset:
void setup()  { 
  // declare pins to be outputs:
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
} 

// the loop routine runs over and over again forever:
void loop(){
  brightness = sin(xStep);
  //map brightness to RGB values
  brightness = brightness * 255;
  //println(brightness);
  analogWrite(redPin, abs(brightness)); //use absolute value for output
  // change the brightness for next time through the loop:
  xStep = xStep + radStep;    
  delay(30);                            
}

