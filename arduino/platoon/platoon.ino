//LED pinouts
int redPin = 3; 
int greenPin = 5; 
int bluePin = 6;
const int pwPin = 10;
double pulse, d; 
//define the range boundaries (lower/upper) for each of the 3 ranges
double ranges[] = {10.0,16.0,17.0,47.0,48.0,70.0};

void setup()  { 
  Serial.begin(19200);  
} 
void loop(){
  //investigate moving this to the setup loop to only do once
  pinMode(pwPin, INPUT);
  pulse = pulseIn(pwPin, HIGH);
  d = pulse/147;
  //cm = inches * 2.54;
  Serial.println(d);
  if (d >= ranges[0] && d <= ranges[1]) {
    int arraySize = 6;
    int LED1_RG1_RED[]   = {28,40,0,40,123,67};
    int LED1_RG1_GREEN[] = {30,93,0,93,35,47};
    int LED1_RG1_BLUE[]  = {68,144,0,144,107,103};
    do { 
      //recalculate distance
      //write to analog pins
      for (int i = 0 ; i <= arraySize ; i++) {
        pulse = pulseIn(pwPin, HIGH);
        d = pulse/147;
        Serial.println("in range 1");
        Serial.println(d);
        Serial.println("----------------");
        Serial.println(ranges[0]);
        Serial.println(ranges[1]);
        if (d < ranges[0] || d > ranges[1]){
          //turn strip off and exit
          analogWrite(redPin, 0); 
          analogWrite(greenPin, 0);
          analogWrite(bluePin, 0);
          break;
        }
        
        analogWrite(redPin, LED1_RG1_RED[i]); 
        analogWrite(greenPin, LED1_RG1_GREEN[i]);
        analogWrite(bluePin, LED1_RG1_BLUE[i]);
        delay(500);
      }
    } while (d >= ranges[0] && d <= ranges[1]);
  } else if (d >= ranges[2] && d <= ranges[3]) {
  
  
  } else if (d >= ranges[4] && d <= ranges[5]) {
  
  } else {
    //do nothing here
  }
}
