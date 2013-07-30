//Code to draw the control center layout

void drawLayout() {
  int xPos    = 10;
  int yPos    = 50;
  int pWidth  = 150;
  int pHeight = 10;
  int labelYPos = 25; 
  for (int i = 0 ; i < numPis ; i++) {
    //Draw color Pickers     
    cPick[i] = cp5[i].addColorPicker("picker"+i,xPos+(i*pWidth)+(i*2*xPos),yPos,pWidth,pHeight)
                     .setColorValue(color(0, 0, 0))
                     ;
    //Draw labels
    String host = "PLTN"+str(i+1);
    hostname[i] = cp5[i].addTextlabel("label")
                        .setText(host+"-"+pHosts.getIp(host))
                        .setPosition(xPos+(i*pWidth)+(i*2*xPos),labelYPos)
                        .setColorValue(#000000)
                        .setFont(createFont("Courier New",12))
                        ;
  }

  background(#545454);
  fill(#cecece);
  rect(5,40,160,300);
}
// println (pHosts.getIp("PLTN4"));
