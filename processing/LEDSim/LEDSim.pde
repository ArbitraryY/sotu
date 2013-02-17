int gradStep = 10;
int arraySize = 3;
int r[] = {255,0,0};
int g[] = {0,255,0};
int b[] = {0,0,255};

void setup(){
  
  
}
void draw(){
  //calculate the differences between each of the elements
  rect(30,20,100,100);
  int diffs[] = {};
  for (int i=0 ; i<arraySize-1 ; i++){
    int rDiff = r[i+1] - r[i];
    int gDiff = g[i+1] - g[i];
    int bDiff = b[i+1] - b[i];
    println("diffs");
    println(rDiff); 
    println(gDiff);
    println(bDiff);
    //set +/- switches
    int plusMinus[] = {0,0,0};
    if (rDiff > 0) {
      plusMinus[0] = 1;
    } else {
      plusMinus[0] = -1;
    }
    if (gDiff > 0) {
      plusMinus[1] = 1;
    } else {
      plusMinus[1] = -1;
    }
    if (bDiff > 0) {
      plusMinus[2] = 1;
    } else {
      plusMinus[2] = -1;
    }
    println("plusMinus array");
    println(plusMinus);
    //println("------------------------");
    //Calculate step sizes
    int steps[] = {0,0,0};
    steps[0] = abs(rDiff / gradStep);
    steps[1] = abs(gDiff / gradStep);
    steps[2] = abs(bDiff / gradStep);
    println("steps: ");
    println(steps); 
    //perform gradient
    int rHold = r[i];
    int gHold = g[i];
    int bHold = b[i];
    println("-------------------");
    for(int j = 0 ; j<gradStep ; j++){
      fill(rHold,gHold,bHold);
      //check for +/-
      if (plusMinus[0] > 0){
        rHold += steps[0];
      } else {
        rHold -= steps[0];
      } 
      if (plusMinus[1] > 0){
        gHold += steps[1];
      } else {
        gHold -= steps[1];
      } 
      if (plusMinus[1] > 0){
        bHold += steps[2];
      } else {
        bHold -= steps[2];
      } 
      println(rHold);
      println(gHold);
      println(bHold);
      delay(50);
    }
    println("-------------------");
    //go to last color
    //analogWrite(r[i],g[i],b[i])
  }
}

void rotateFunc(){
  

}
