//Textlabel hostname;

//create ControlP5 objects
void createObjs(){
  for (int i=0 ; i < numPis ; i++) {
    cp5[i]   = new ControlP5(this);
    //cPick[i] = new ColorPicker();
  } 
  
}

//ColorPicker objects for each unit
/*ColorPicker cPick1;
ColorPicker cPick2;
ColorPicker cPick3;
ColorPicker cPick4;
ColorPicker cPick5;
ColorPicker cPick6;*/

//OSC objects for each unit
OscP5 osc1;
OscP5 osc2;
OscP5 osc3;
OscP5 osc4;
OscP5 osc5;
OscP5 osc6;

//NetAddress objs for each server
NetAddress oscServer;
