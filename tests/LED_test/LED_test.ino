//LED pinouts
int redPin1      = 3;//LED1 red pin
int greenPin1    = 5;//LED1 green pin
int bluePin1     = 6;//LED1 bluepin

int redPin2      = 9;//LED1 red pin
int greenPin2    = 10;//LED1 green pin
int bluePin2     = 11;//LED1 bluepin

void setup()  { 
  Serial.begin(19200);  
} 
void loop(){
  analogWrite(redPin1,255);
  analogWrite(bluePin1,0);
  analogWrite(greenPin1,0);
  
  analogWrite(redPin2,255);
  analogWrite(bluePin2,0);
  analogWrite(greenPin2,0);
  delay(1000);
  analogWrite(redPin1,0);
  analogWrite(bluePin1,255);
  analogWrite(greenPin1,0);
  analogWrite(redPin2,0);
  analogWrite(bluePin2,255);
  analogWrite(greenPin2,0);
  delay(1000);
  analogWrite(redPin1,0);
  analogWrite(bluePin1,0);
  analogWrite(greenPin1,255);
  analogWrite(redPin2,0);
  analogWrite(bluePin2,0);
  analogWrite(greenPin2,255);
  delay(1000);
}
