
int numPis = 6;

//Control P5 Objects for each unit
ControlP5[] cp = new ControlP5[numPis];

//println ("test");
/*
for (int i=0 ; i <= numPis ; i++) {
  cp[i] = new ControlP5();
}*/
/*
ControlP5 cp1;
ControlP5 cp2;
ControlP5 cp3;
ControlP5 cp4;
ControlP5 cp5;
ControlP5 cp6;*/

Textlabel hostname;

//ColorPicker objects for each unit
ColorPicker cPick1;
ColorPicker cPick2;
ColorPicker cPick3;
ColorPicker cPick4;
ColorPicker cPick5;
ColorPicker cPick6;

//OSC objects for each unit
OscP5 osc1;
OscP5 osc2;
OscP5 osc3;
OscP5 osc4;
OscP5 osc5;
OscP5 osc6;

//NetAddress objs for each server
NetAddress oscServer;
