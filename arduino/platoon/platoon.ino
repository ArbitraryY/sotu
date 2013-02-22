//LED pinouts
int redPin      = 3;//LED1 red pin
int greenPin    = 5;//LED1 green pin
int bluePin     = 6;//LED1 bluepin
int FADESPEED   = 0;
const int pwPin = 10;
double pulse, d; 
//define the range boundaries (lower/upper) for each of the 3 ranges
double ranges[] = {10.0,16.0,17.0,47.0,48.0,70.0};

void setup()  { 
  Serial.begin(19200);  
} 
void loop(){
  //investigate moving this to the setup loop to only do once
  //pinMode(analogPin,INPUT);
  pinMode(pwPin, INPUT);
  pulse = pulseIn(pwPin, HIGH);
  d = pulse/147;
  //cm = inches * 2.54;
  Serial.println(d);
  if (d >= ranges[0] && d <= ranges[1]) {
    int arraySize = 6;
    int LED1_RG1_RED[]   = {28,40,255,40,123,67};
    int LED1_RG1_GREEN[] = {30,93,255,93,35,47};
    int LED1_RG1_BLUE[]  = {68,144,255,144,107,103};
    do {
      //write to analog pins
      //reinitialize i if it gets above intended size.  Runs wild after that!!!
      for (int i = 0 ; i < arraySize ; i++) {
        //recalculate distance inside do..while need to exit loop if exit range
        pulse = pulseIn(pwPin, HIGH);
        //calculate distance in inches
        d = pulse/147;
        Serial.println("in range 1");
        Serial.println(d);
        Serial.println("----------------");
       // Serial.println(ranges[0]);
        //Serial.println(ranges[1]);
        Serial.print("RED LED: ");
        Serial.println(LED1_RG1_RED[i]);
        Serial.print("GREEN LED: ");
        Serial.println(LED1_RG1_GREEN[i]);
        Serial.print("BLUE LED: ");
        Serial.println(LED1_RG1_BLUE[i]);
        //pause between iterations to check RGB values. increase to 5000 for best view
        delay(5);
        if (d < ranges[0] || d > ranges[1]){
          //turn strip off and exit
          analogWrite(redPin, 0); 
          analogWrite(greenPin, 0);
          analogWrite(bluePin, 0);
          break;
        }
        //fade LEDs
        if (LED1_RG1_RED[i] > LED1_RG1_RED[i+1]){
           do{ 
             analogWrite(redPin, LED1_RG1_RED[i]);
             LED1_RG1_RED[i]--;
             Serial.println(LED1_RG1_RED[i]);
             delay(FADESPEED);
           } while(LED1_RG1_RED[i] > LED1_RG1_RED[i+1]); 
        } else {
          do{ 
             analogWrite(redPin, LED1_RG1_RED[i]);
             LED1_RG1_RED[i]++;
             Serial.println(LED1_RG1_RED[i]);
             delay(FADESPEED);
           } while(LED1_RG1_RED[i] < LED1_RG1_RED[i+1]);
        }
        
        if (LED1_RG1_GREEN[i] > LED1_RG1_GREEN[i+1]){
           do{ 
             analogWrite(greenPin, LED1_RG1_GREEN[i]);
             LED1_RG1_GREEN[i]--;
             Serial.println(LED1_RG1_GREEN[i]);
             delay(FADESPEED);
           } while(LED1_RG1_GREEN[i] > LED1_RG1_GREEN[i+1]); 
        } else {
          do{ 
             analogWrite(greenPin, LED1_RG1_GREEN[i]);
             LED1_RG1_GREEN[i]++;
             Serial.println(LED1_RG1_GREEN[i]);
             delay(FADESPEED);
           } while(LED1_RG1_GREEN[i] < LED1_RG1_GREEN[i+1]);
        }
        if (LED1_RG1_BLUE[i] > LED1_RG1_BLUE[i+1]){
           do{ 
             analogWrite(bluePin, LED1_RG1_BLUE[i]);
             LED1_RG1_BLUE[i]--;
             Serial.println(LED1_RG1_BLUE[i]);
             delay(FADESPEED);
           } while(LED1_RG1_BLUE[i] > LED1_RG1_BLUE[i+1]); 
        } else {
          do{ 
             analogWrite(bluePin, LED1_RG1_BLUE[i]);
             LED1_RG1_BLUE[i]++;
             Serial.println(LED1_RG1_BLUE[i]);
             delay(FADESPEED);
           } while(LED1_RG1_BLUE[i] < LED1_RG1_BLUE[i+1]);
        }
      }
    } while (d >= ranges[0] && d <= ranges[1]);
  } else if (d >= ranges[2] && d <= ranges[3]) {
  
  
  } else if (d >= ranges[4] && d <= ranges[5]) {
  
  } else {
    //do nothing here
  }
}
