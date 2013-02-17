const float pi = 3.14;

//LED pinouts
int redPin = 3; 
int greenPin = 5; 
int bluePin = 6;
const int pwPin = 10;
double pulse, inches, cm;

// the setup routine runs once when you press reset:
void setup()  { 
  Serial.begin(19200);  
} 

// the loop routine runs over and over again forever:
void loop(){
  pinMode(pwPin, INPUT);
  pulse = pulseIn(pwPin, HIGH);
  inches = pulse/147;
  cm = inches * 2.54;
  
  
  //int randGreen = random(0,255);
  //int randBlue = random(0,255);
  //int randRed = random(0,255);
  
  if (inches > 10.0 && inches < 34.0) {
    analogWrite(redPin, 255); 
    analogWrite(greenPin, 0);
    analogWrite(bluePin, 0);
  } else if (inches >= 34.0 && inches < 67.0) {
    analogWrite(redPin, 0); 
    analogWrite(greenPin, 255);
    analogWrite(bluePin, 0);
  } else if (inches >= 67.0 && inches < 101.0) {
    analogWrite(redPin, 0); 
    analogWrite(greenPin, 0);
    analogWrite(bluePin, 255);
  } else {
    analogWrite(redPin, 0); 
    analogWrite(greenPin, 0);
    analogWrite(bluePin, 0);
  }
  
  
  Serial.print(inches);
  Serial.print("in, ");
  Serial.print(cm);
  Serial.print("cm");
  Serial.println();
  /*Serial.print("int(abs(blueBrightness)) = ");
  Serial.println(int(abs(randBlue)));
  Serial.print("int(abs(greenBrightness)) = ");
  Serial.println(int(abs(randGreen)));
  Serial.print("int(abs(redBrightness)) = ");
  Serial.println(int(abs(randRed)));*/
  Serial.println("------------------------");           

  delay(500);  
}

