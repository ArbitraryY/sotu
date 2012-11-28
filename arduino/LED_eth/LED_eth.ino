const float pi = 3.14;

//LED pinouts
int redPin = 3; 
int greenPin = 5; 
int bluePin = 6;
float brightness = 0.0;    // how bright the LED is
int fadeAmount = 5;    // how many points to fade the LED by
float xStep = 0;
float radStep = pi/250; //step amount in radians

// the setup routine runs once when you press reset:
void setup()  { 
  Serial.begin(9600);  
  // declare pins to be outputs:
  pinMode(redPin, OUTPUT);
  //pinMode(greenPin, OUTPUT);
  //pinMode(bluePin, OUTPUT);
} 
//void loop(){
//  analogWrite(redPin, 0);
//}
// the loop routine runs over and over again forever:
void loop(){
  brightness = sin(xStep);
  //map brightness to RGB values
  brightness = abs(int(brightness * 255));
  //Absolute value of brightness to output
  analogWrite(redPin, brightness); 
  if (int(brightness == 0)){
    analogWrite(redPin,LOW);
    delay(5000);
  }
  Serial.print("xStep = ");
  Serial.println(xStep);
  Serial.print("sin(xStep) = ");
  Serial.println(sin(xStep));
  Serial.print("int(abs(Brightness)) = ");
  Serial.println(int(abs(brightness)));
  Serial.println("------------------------");
  // change the brightness for next time through the loop:
  xStep = xStep + radStep; 
  delay(5);                        
}

