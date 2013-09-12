//Code to draw the control center layout

void drawLayout() {
  int xPos      = 10;
  int yPos      = 50;
  int pWidth    = 150;
  int pHeight   = 10;
  int labelYPos = 25;
  int bangIdSeed = 10;
  int statusHeadingYPos = 185;
  for (int i = 0 ; i < numPis ; i++) {
    //Draw color Pickers     
    cPick[i] = cp5[i].addColorPicker("picker",xPos+(i*pWidth)+(i*xPos),yPos,pWidth,pHeight)
                     //.setColorValue(color(1.0, 1.0, 1.0))
                     .setId(i)
                     ;
    println(cPick[i].getId());
    //Draw labels
    String host = "PLTN"+str(i+1);
    hostname[i] = cp5[i].addTextlabel("label")
                        .setText(host+"  ( "+pHosts.getIp(host)+" )")
                        .setPosition(xPos+(i*pWidth)+(i*xPos),labelYPos)
                        .setColorValue(#ffffff)
                        ;
    //draw shutdown buttons
     cp5[i].addBang("allOn")
       .setPosition(xPos+2+(i*pWidth)+(i*xPos), 120)
       .setSize(pWidth-5, 20)
       .setId(i)
       ;
     cp5[i].addBang("allOff")
       .setPosition(xPos+2+(i*pWidth)+(i*xPos), 160)
       .setSize(pWidth-5, 20)
       .setId(i)
       ;
    cp5[i].addBang("shutdown")
       .setPosition(xPos+2+(i*pWidth)+(i*xPos), 200)
       .setSize(pWidth-5, 20)
       .setId(i)
       ;
    //Status panel
    /*fill(#ffffff);
    text("status",xPos+2+(i*pWidth)+(i*xPos),statusHeadingYPos);
    text("osc:",xPos+2+(i*pWidth)+(i*xPos),statusHeadingYPos+15);
    text("ssh:",xPos+2+(i*pWidth)+(i*xPos),statusHeadingYPos+30);
    text("http:",xPos+2+(i*pWidth)+(i*xPos),statusHeadingYPos+45);
    text("agent:",xPos+2+(i*pWidth)+(i*xPos),statusHeadingYPos+60);
    text("scheme:",xPos+2+(i*pWidth)+(i*xPos),statusHeadingYPos+75);*/
    //fill(#521FED);
    //rect(xPos+(i*pWidth)+(i*xPos), yPos+130, pWidth, 100);
  }
}
