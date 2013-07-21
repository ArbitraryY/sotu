//Code to draw the control center layout

void drawLayout() {
  //ControlP5[] cps = new ControlP5;
  /*cp1 = new ControlP5(this); 
  cp2 = new ControlP5(this);
  cp3 = new ControlP5(this); 
  cp4 = new ControlP5(this); 
  cp5 = new ControlP5(this); 
  cp6 = new ControlP5(this);*/
  
  hostname = cp[1].addTextlabel("label")
                .setText("PLTN1")
                .setPosition(10,30)
                .setColorValue(#000000)
                .setFont(createFont("Courier New",12))
                ;
  hostname = cp[2].addTextlabel("label")
                .setText("PLTN2")
                .setPosition(170,30)
                .setColorValue(#000000)
                .setFont(createFont("Courier New",12))
                ;
  cPick1 = cp[1].addColorPicker("picker",10,50,150,10)
              .setColorValue(color(0, 0, 0))
              ;
  cPick2 = cp[2].addColorPicker("picker",170,50,150,10)
              .setColorValue(color(0, 0, 0))
              ;

  background(#545454);
  fill(#cecece);
  rect(5,40,160,300);
}
// println (pHosts.getIp("PLTN4"));
