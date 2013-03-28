//LED pinouts
int redPin1      = 3;//LED1 red pin
int redPin2      = 9;//LED2 red pin
int greenPin1    = 5;//LED1 green pin
int greenPin2    = 10;//LED2 green pin
int bluePin1     = 6;//LED1 bluePin1
int bluePin2     = 11;//LED2 bluePin1

int FADESPEED   = 0;
const int pwPin = 8;
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
    int ledColorsArraySize1 = 6;
    int ledColorsArraySize2 = 5;
    
    int LED1_RG1_RED[]   = {28,40,255,40,123,67};
    int LED1_RG1_GREEN[] = {30,93,255,93,35,47};
    int LED1_RG1_BLUE[]  = {68,144,255,144,107,103};
    
    int LED2_RG1_RED[]   = {150,32,121,255,238};
    int LED2_RG1_GREEN[]   = {44,69,65,255,68};
    int LED2_RG1_BLUE[]   = {37,97,137,255,79};
    
    //write initial color values to strips
    analogWrite(redPin1, LED1_RG1_RED[0]); 
    analogWrite(greenPin1, LED1_RG1_GREEN[0]);
    analogWrite(bluePin1, LED1_RG1_BLUE[0]);
    analogWrite(redPin2, LED2_RG1_RED[0]); 
    analogWrite(greenPin2, LED2_RG1_GREEN[0]);
    analogWrite(bluePin2, LED2_RG1_BLUE[0]);
    
    do {
      //write to analog pins
      //reinitialize i if it gets above intended size.  Runs wild after that!!!
      for (int i = 0 ; i < ledColorsArraySize1 ; i++) {
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
          analogWrite(redPin1, 0); 
          analogWrite(greenPin1, 0);
          analogWrite(bluePin1, 0);
          analogWrite(redPin2, 0); 
          analogWrite(greenPin2, 0);
          analogWrite(bluePin2, 0);
          break;
        }
        //fade red LED strip 1
        if (LED1_RG1_RED[i] > LED1_RG1_RED[i+1]){
           do{ 
             analogWrite(redPin1, LED1_RG1_RED[i]);
             LED1_RG1_RED[i]--;
             Serial.println(LED1_RG1_RED[i]);
             delay(FADESPEED);
           } while(LED1_RG1_RED[i] > LED1_RG1_RED[i+1]); 
        } else {
          do{ 
             analogWrite(redPin1, LED1_RG1_RED[i]);
             LED1_RG1_RED[i]++;
             Serial.println(LED1_RG1_RED[i]);
             delay(FADESPEED);
           } while(LED1_RG1_RED[i] < LED1_RG1_RED[i+1]);
        }
        //end fade red strip 1
        //fade red LED strip 2
        if (LED2_RG1_RED[i] > LED2_RG1_RED[i+1]){
           do{ 
             analogWrite(redPin2, LED2_RG1_RED[i]);
             LED2_RG1_RED[i]--;
             Serial.println(LED2_RG1_RED[i]);
             delay(FADESPEED);
           } while(LED2_RG1_RED[i] > LED2_RG1_RED[i+1]); 
        } else {
          do{ 
             analogWrite(redPin2, LED2_RG1_RED[i]);
             LED2_RG1_RED[i]++;
             Serial.println(LED2_RG1_RED[i]);
             delay(FADESPEED);
           } while(LED2_RG1_RED[i] < LED2_RG1_RED[i+1]);
        }
        //end fade red LED strip 2
        //begin fade green strip 1      
        if (LED1_RG1_GREEN[i] > LED1_RG1_GREEN[i+1]){
           do{ 
             analogWrite(greenPin1, LED1_RG1_GREEN[i]);
             LED1_RG1_GREEN[i]--;
             Serial.println(LED1_RG1_GREEN[i]);
             delay(FADESPEED);
           } while(LED1_RG1_GREEN[i] > LED1_RG1_GREEN[i+1]); 
        } else {
          do{ 
             analogWrite(greenPin1, LED1_RG1_GREEN[i]);
             LED1_RG1_GREEN[i]++;
             Serial.println(LED1_RG1_GREEN[i]);
             delay(FADESPEED);
           } while(LED1_RG1_GREEN[i] < LED1_RG1_GREEN[i+1]);
        }
        //end fade green LED strip 1
        //begin fade green strip 2
        if (LED2_RG1_GREEN[i] > LED2_RG1_GREEN[i+1]){
           do{ 
             analogWrite(greenPin2, LED2_RG1_GREEN[i]);
             LED2_RG1_GREEN[i]--;
             Serial.println(LED2_RG1_GREEN[i]);
             delay(FADESPEED);
           } while(LED2_RG1_GREEN[i] > LED2_RG1_GREEN[i+1]); 
        } else {
          do{ 
             analogWrite(greenPin2, LED2_RG1_GREEN[i]);
             LED2_RG1_GREEN[i]++;
             Serial.println(LED2_RG1_GREEN[i]);
             delay(FADESPEED);
           } while(LED2_RG1_GREEN[i] < LED2_RG1_GREEN[i+1]);
        }
        //end fade green strip 2
        //begin fade blue strip 1        
        if (LED1_RG1_BLUE[i] > LED1_RG1_BLUE[i+1]){
           do{ 
             analogWrite(bluePin1, LED1_RG1_BLUE[i]);
             LED1_RG1_BLUE[i]--;
             Serial.println(LED1_RG1_BLUE[i]);
             delay(FADESPEED);
           } while(LED1_RG1_BLUE[i] > LED1_RG1_BLUE[i+1]); 
        } else {
          do{ 
             analogWrite(bluePin1, LED1_RG1_BLUE[i]);
             LED1_RG1_BLUE[i]++;
             Serial.println(LED1_RG1_BLUE[i]);
             delay(FADESPEED);
           } while(LED1_RG1_BLUE[i] < LED1_RG1_BLUE[i+1]);
        }
        //end fade blue LED strip1
        //Begin fade blue LED strip 2
        if (LED2_RG1_BLUE[i] > LED2_RG1_BLUE[i+1]){
           do{ 
             analogWrite(bluePin2, LED2_RG1_BLUE[i]);
             LED2_RG1_BLUE[i]--;
             Serial.println(LED2_RG1_BLUE[i]);
             delay(FADESPEED);
           } while(LED2_RG1_BLUE[i] > LED2_RG1_BLUE[i+1]); 
        } else {
          do{ 
             analogWrite(bluePin2, LED2_RG1_BLUE[i]);
             LED2_RG1_BLUE[i]++;
             Serial.println(LED2_RG1_BLUE[i]);
             delay(FADESPEED);
           } while(LED2_RG1_BLUE[i] < LED2_RG1_BLUE[i+1]);
        }
        //end fade blue LED strip 2       
      }
    } while (d >= ranges[0] && d <= ranges[1]);
  } else if (d >= ranges[2] && d <= ranges[3]) {
  
  
  } else if (d >= ranges[4] && d <= ranges[5]) {
  
  } else {
    //do nothing here
  }
}
