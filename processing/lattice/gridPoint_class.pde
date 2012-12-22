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
