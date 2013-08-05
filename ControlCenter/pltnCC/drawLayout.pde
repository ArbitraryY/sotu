//Code to draw the control center layout

void drawLayout() {
  int xPos      = 10;
  int yPos      = 50;
  int pWidth    = 150;
  int pHeight   = 10;
  int labelYPos = 25;
  for (int i = 0 ; i < numPis ; i++) {
    //Draw color Pickers     
    cPick[i] = cp5[i].addColorPicker("picker"+i,xPos+(i*pWidth)+(i*xPos),yPos,pWidth,pHeight)
                     .setColorValue(color(0, 0, 0))
                     ;
    //Draw labels
    String host = "PLTN"+str(i+1);
    hostname[i] = cp5[i].addTextlabel("label")
                        .setText(host+"-"+pHosts.getIp(host))
                        .setPosition(xPos+(i*pWidth)+(i*xPos),labelYPos)
                        .setColorValue(#ffffff)
                        .setFont(createFont("Courier New",12))
                        ;
    //Draw Backgrounds
    //region[i].drawIt(i);
    stroke(2);
    rect(xPos+(i*pWidth)+(i*xPos), yPos, pWidth, 200);
    //draw buttons
    cp5[i].addBang("shutdown")
       .setPosition(xPos+5+(i*pWidth)+(i*xPos), 130)
       .setSize(pWidth-10, 20)
       .setId(i)
       ;
    //r.drawIt(2);
  }
}
