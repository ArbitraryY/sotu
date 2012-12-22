int win_width     = 700; //window width
int win_height    = 700; //window height
int grid_pt_width = 100; //the distance between grid points
int grid_color    = 79; //grid line colors
int bg_color      = 0; //Background color
boolean show_grid = false; //whether or not (true/false) to show the grid
int r_max         = grid_pt_width / 2; //Maximum size of the radius for a given circle
int r_min         = grid_pt_width / 10; //Minimum size of the radius for a given circle
int number_of_shapes = ((win_width-grid_pt_width) / grid_pt_width) * ((win_height-grid_pt_width) / grid_pt_width); //Number of shapes in the dot array
int [][] grid_pos; //array for positions on grid
String red_fill   = "204,51,0"; //Red fill color
int redraw_count = 0;
int redraw_max  = 37; //number of times to iterate before drawing final lattice

class GridPoint {
    int x_pos;
    int y_pos;
    
    GridPoint(int x_pos_, int y_pos_){
      x_pos = x_pos_;
      y_pos = y_pos_;
    }
    void display(){
      print("x=");
      println(x_pos);
      print("y=");
      println(y_pos);
    }
    int get_x(){
      return x_pos;
    }
    int get_y(){
      return y_pos;
    }
  }

GridPoint[] grid_points = new GridPoint[number_of_shapes];

void setup(){ 
  size(win_width,win_height);
  background(bg_color);
  print("Total number of shapes = ");
  println(number_of_shapes);
  //noLoop();//prevents next loop iteration
  int redraw_count = 0;
}

void draw(){
  //draw grid lines
  if (show_grid){
    for (int i=grid_pt_width ; i<=(win_width) ; i=i+grid_pt_width){
      //draw vertical lines
      line(i, grid_pt_width, i, win_width-grid_pt_width);
      stroke(grid_color);
    } 
    for (int i=grid_pt_width ; i<(win_height) ; i=i+grid_pt_width){
      //draw horizontal lines
      line(grid_pt_width, i, win_height-grid_pt_width, i);
      stroke(grid_color);
    }
  }
  else{
    //Do nothing
  }
  //generate filled circles
  int i = 0;//array of objects index
  //loop through x grid points
  for (int x=grid_pt_width ; x<win_height ; x=x+grid_pt_width){
    //loop through y rgid points
    for (int y=grid_pt_width ; y<win_width ; y=y+grid_pt_width) {
      //randomly generate the ellipse color
      int ec = 0;
      //random 1 or 0
      int ellipse_color = int(random(0,2));
      if (ellipse_color == 0){
        ec = 102;
      } else {
        ec = 255;
      }
      //generate radius for ellipse (value between r_min and r_max)
      float this_radius = random(r_min,r_max);
      ellipseMode(RADIUS);
      fill(ec);
      ellipse(x,y,this_radius,this_radius);
      print("-------------\n");
      println(i); 
      //put x and y values in each object
      grid_points[i] = new GridPoint(x,y);
      grid_points[i].display();
      //iterate array index    
      i=i+1;
    } 
  }
  //random position for the (+)
  int plus_position = int(random(0,number_of_shapes));
  //draw red ellipse of r_max at this position
  fill(204,51,0);
  ellipse(grid_points[plus_position].get_x(),grid_points[plus_position].get_y(),r_max,r_max);
  //draw horizontal line for +
  strokeWeight(11);
  line(grid_points[plus_position].get_x()-(r_max / 2),grid_points[plus_position].get_y(),grid_points[plus_position].get_x()+(r_max / 2),grid_points[plus_position].get_y());
  //draw vertical line for +
  line(grid_points[plus_position].get_x(),grid_points[plus_position].get_y()-(r_max / 2),grid_points[plus_position].get_x(),grid_points[plus_position].get_y()+(r_max / 2));
  println("-------------");
  println(grid_points[plus_position].get_x());
  println(grid_points[plus_position].get_y());
  print("plus_pos = ");
  println(plus_position+1);
  //Only draw the "redraw_max"th drawing 
  if (redraw_count != redraw_max) {
    background(bg_color);
    print("redraw_count = ");
    println(redraw_count);
    print("redraw_max = ");
    println(redraw_max);
    redraw_count++;
    redraw();
  } else {
    noLoop();
  }
  
}

/*void mousePressed(){
  background(bg_color);  
  redraw();
}*/
