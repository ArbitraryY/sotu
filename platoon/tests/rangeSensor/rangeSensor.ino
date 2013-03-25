const int pwPin = 8;
const int anPin = 0;
double pulse, d; 
float anVolt;

void setup()  { 
  Serial.begin(19200);  
} 
void loop(){
  pinMode(pwPin, INPUT);
  pinMode(anPin, INPUT);
  
  anVolt = analogRead(anPin);
  pulse = pulseIn(pwPin, HIGH);
  d = pulse/147;
  //cm = inches * 2.54;
  //Serial.println(d);
  Serial.println(anVolt);
  delay(5);
}
