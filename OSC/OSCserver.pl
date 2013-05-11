#!/usr/bin/perl

use strict;
use Net::OpenSoundControl::Server;
my $port = 4567;

use Data::Dumper qw(Dumper);

sub ledAction {
   	#re-initialize each variable for each cal to ledAction 
    my $color   = '';
    my $rpiCmd  = '';
    my $pltnCmd = '';
    my $srvcCmd = '';
    
    my $oscMsgRef  = $_[1]; #assign OSC msg reference to var
    my $oscAddress = "@{ $oscMsgRef }[0]";
    my $oscType    = "@{ $oscMsgRef }[1]";
    my $oscValue   = "@{ $oscMsgRef }[2]";
    #print Dumper $oscMsgRef;
    print "Address:" . "$oscAddress\n" ;
    print "Type:" . "$oscType\n" ;
    print "Value:" . "$oscValue\n\n";
    
    #parse commands from OSC addresses
    $oscAddress =~ m/\/led\/(\w+)/;
    $color = $1;

	$oscAddress =~ m/\/rpi\/(\w+)/;
	$rpiCmd = $1;
    
	$oscAddress =~ m/\/pltn\/(\w+)/;
	$pltnCmd = $1;
	
	$oscAddress =~ m/\/srvc\/(\S+)/;
	$srvcCmd = $1;
	
    #hash of colors and corresponding GPIO on RPi
    my %ledGPIO = (
	     red1   => "2", #GPIO 18 
		 green1 => "5", #     23
		 blue1  => "7", #     25
		 red2   => "1", #     17
		 green2 => "4", #     22
		 blue2  => "6", #     24
	);
    # LED (/led) OSC commands 
    if ($oscAddress =~ 'led') {
    	#Set to all white
    	if ($color eq 'white') {
    		my $colorPerc = 0.00001;
			foreach my $key ( keys %ledGPIO )
			{ 
    			system("echo \"$ledGPIO{$key}=$colorPerc\" > /dev/pi-blaster"); 
   			}	
    	#Turn all LEDs off
    	} elsif ($color eq 'allOff') {
			foreach my $key ( keys %ledGPIO )
			{ 
    			system("echo \"$ledGPIO{$key}=0\" > /dev/pi-blaster"); 
   			}	
    	# set LED color according to passed pin value
    	} else {
    		system("echo \"$ledGPIO{$color}=$oscValue\" > /dev/pi-blaster"); 
    	}
    }
    
    #Handle services (/srvc) OSC commands
    if ($oscAddress =~ 'srvc') {
    	my $sysCmd = '';
    	if ($oscValue == 1){
    		$sysCmd = "sudo service " . $srvcCmd . " start"; 
    	} elsif ($oscValue == 0){
    		$sysCmd = "sudo service " . $srvcCmd . " stop"; 
    	} else{
		   	print "not a valid /srvc OSC address";	
    	}
    	system $sysCmd;	
    	print "sysCmd: " . $sysCmd ."\n";
    }
    
	#Handle RPi (/rpi) PSC Commands
	if ($oscAddress =~ 'rpi') {
    	my $sysCmd = '';
   		if ($rpiCmd eq 'off') {
			print "Shutting Down the Raspberry Pi";
			for (my $i = 0; $i <= 5; $i++) {
				print ".";
				sleep (1);
			}
			$sysCmd = 'sudo shutdown -h now';
    	} else {
    		print "Not a valid RPi OSC command\n"
    	}
    	#run the system command
   		system $sysCmd;
	}  
}

my $server =
    Net::OpenSoundControl::Server->new(Port => $port, Handler => \&ledAction)
    or die "Could not start server: $@\n";

print "[OSC Server] Receiving messages on port $port\n";

$server->readloop();
print $server->port();
