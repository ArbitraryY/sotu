//import java.util.Map;

class PltnHosts {
  HashMap<String,String> hosts = new HashMap<String,String>();
  //Hashmap of pltn ips
  
  PltnHosts(){ //the constructor
    //hosts.put("PLTN1","192.168.1.71");
    hosts.put("PLTN1","localhost");
    //hosts.put("PLTN2","192.168.1.72");
    hosts.put("PLTN2","localhost");
    hosts.put("PLTN3","192.168.1.73");
    hosts.put("PLTN4","192.168.1.74");
    hosts.put("PLTN5","192.168.1.75");
    hosts.put("PLTN6","192.168.1.76");
  }
  //Return the IP address based on hostname
  String getIp(String host){
    return hosts.get(host);
  }
}

  // Using an enhanced loop to interate over each entry
//  for (Map.Entry ip : pltnIps.entrySet()) {
///    print(ip.getKey() + " is ");
//    println(ip.getValue());
//  }

class DrawRegions{
  //This class draws the regions behind each Color Picker
  int rWidth = 160;
  int rStart = 5; 
  DrawRegions(){
    int test;
    //The constructor
  }
  void drawIt(int i){
    int xPos = i*rWidth + rStart;
    background(#545454);
    fill(#cecece);
    rect(xPos,40,rWidth,300);
  }
}

