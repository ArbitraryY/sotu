int win_width  = 800;
int win_height = 800;
color c1       = #cc3300;
color bg       = #000000;
int num_rects  = 5;

/*class drawRect {
    int x;
    
    drawRect(int x_){
      x_pos = x_;
    }
}*/

//drawRect[] x = new drawRect[var];

void setup(){
  size(win_width,win_height);
  background(bg);
}

void draw(){
  int i = 0;
  stroke(#CC3300);
  fill(bg);
  for (i=0 ; i<num_rects ; i++){
    rect(100,100,win_width-200,win_height-200);
    println(i);
  }
  noLoop();
} 


