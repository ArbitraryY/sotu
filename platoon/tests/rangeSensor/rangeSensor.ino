const int pwPin = 8;
double pulse, d; 

void setup()  { 
  Serial.begin(19200);  
} 
void loop(){
  pinMode(pwPin, INPUT);
  pulse = pulseIn(pwPin, HIGH);
  d = pulse/147;
  //cm = inches * 2.54;
  Serial.println(d);
  delay(2);
}
