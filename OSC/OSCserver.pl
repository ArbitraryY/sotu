#!/usr/bin/perl

use strict;
use Net::OpenSoundControl::Server;
my $port = 4567;

use Data::Dumper qw(Dumper);

sub ledAction {
    my $oscMsgRef  = $_[1]; #assign OSC msg reference to var
    my $oscAddress = "@{ $oscMsgRef }[0]";
    my $oscType    = "@{ $oscMsgRef }[1]";
    my $oscValue   = "@{ $oscMsgRef }[2]";
    #print Dumper $oscMsgRef;
    print "Address:" . "$oscAddress\n" ;
    print "Type:" . "$oscType\n" ;
    print "Value:" . "$oscValue\n\n";
   
    #parse color from OSC address
    $oscAddress =~ m/\/led\/(\w+)/;
    my $color = $1;

	$oscAddress =~ m/\/rpi\/(\w+)/;
	my $oscCmd = $1;
    
	$oscAddress =~ m/\/pltn\/(\w+)/;
	my $oscCmd = $1;
	
    #hash of colors and corresponding GPIO on RPi
    my %ledGPIO = (
		red1   => "2", #GPIO 23
		green1 => "5", #     18
		blue1  => "7", #     24
		red2   => "1", #     24
		green2 => "4", #     24
		blue2  => "6", #     24
	       );
    
    if ($color eq 'white') {
    	my $colorPerc = 0.00001;
		foreach my $key ( keys %ledGPIO )
		{ 
    		system("echo \"$ledGPIO{$key}=$colorPerc\" > /dev/pi-blaster"); 
   		}	
    }
    if ($color eq 'allOff') {
		foreach my $key ( keys %ledGPIO )
		{ 
    		system("echo \"$ledGPIO{$key}=0\" > /dev/pi-blaster"); 
   		}	
    }
    if ($oscCmd eq 'off') {
		print "Shutting Down the Raspberry Pi";
		for (my $i = 0; $i <= 5; $i++) {
			print ".";
			sleep (1);
		}
		my $shutdownCmd = 'sudo shutdown -h now';
    	system $shutdownCmd;
    }
    if ($oscCmd eq 'rngSnsr') {
    	my $cmd = '';
    	if ($oscValue == 0){
    		print "Shutting down the range sensor\n";
    		$cmd = 'service rangeSensor stop';
    	} elsif ($oscValue == 1) {
    		$cmd = 'service rangeSensor start &';
    	}
	    system $cmd;
    }
    
    #write to device file
    system("echo \"$ledGPIO{$color}=$oscValue\" > /dev/pi-blaster"); 
}

my $server =
    Net::OpenSoundControl::Server->new(Port => $port, Handler => \&ledAction)
    or die "Could not start server: $@\n";

print "[OSC Server] Receiving messages on port $port\n";

$server->readloop();
print $server->port();
