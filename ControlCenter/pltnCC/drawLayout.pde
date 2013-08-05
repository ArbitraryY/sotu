//Code to draw the control center layout

void drawLayout() {
  int xPos      = 10;
  int yPos      = 50;
  int pWidth    = 150;
  int pHeight   = 10;
  int labelYPos = 25;
  int statusHeadingYPos = 185;
  for (int i = 0 ; i < numPis ; i++) {
    //Draw color Pickers     
    cPick[i] = cp5[i].addColorPicker("picker"+i,xPos+(i*pWidth)+(i*xPos),yPos,pWidth,pHeight)
                     .setColorValue(color(0, 0, 0))
                     ;
    //Draw labels
    String host = "PLTN"+str(i+1);
    hostname[i] = cp5[i].addTextlabel("label")
                        .setText(host+"  ( "+pHosts.getIp(host)+" )")
                        .setPosition(xPos+(i*pWidth)+(i*xPos),labelYPos)
                        .setColorValue(#ffffff)
                        //.setFont(createFont("Courier New",12))
                        ;
    //Draw Backgrounds
    //region[i].drawIt(i);
    
    //draw buttons
    cp5[i].addBang("shutdown")
       .setPosition(xPos+2+(i*pWidth)+(i*xPos), 130)
       .setSize(pWidth-10, 20)
       .setId(i)
       ;
    //Status panel
    fill(#ffffff);
    text("status",xPos+2+(i*pWidth)+(i*xPos),statusHeadingYPos);
    text("osc:",xPos+2+(i*pWidth)+(i*xPos),statusHeadingYPos+15);
    text("ssh:",xPos+2+(i*pWidth)+(i*xPos),statusHeadingYPos+30);
    text("http:",xPos+2+(i*pWidth)+(i*xPos),statusHeadingYPos+45);
    text("agent:",xPos+2+(i*pWidth)+(i*xPos),statusHeadingYPos+60);
    text("scheme:",xPos+2+(i*pWidth)+(i*xPos),statusHeadingYPos+75);
    //fill(#521FED);
    //rect(xPos+(i*pWidth)+(i*xPos), yPos+130, pWidth, 100);
  }
}

/*void picker1(int col) {
  println("picker\talpha:"+alpha(col)+"\tred:"+red(col)+"\tgreen:"+green(col)+"\tblue:"+blue(col)+"\tcol"+col);
}*/

/*public void controlEvent(ControlEvent theEvent) {
  for (int i=0;i<col.length;i++) {
    if (theEvent.getController().getName().equals("bang"+i)) {
      col[i] = color(random(255));
    }
  }
}*/