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
    #print "Color: " . $color . "\n";
    #hash of colors and corresponding GPIO on RPi
    my %ledGPIO = (
		red   => "2", #GPIO 23
		green => "4", #     18
		blue  => "6", #     24
	       );
    #print the GPIO color from hash map
    #print "GPIO value: " . $ledGPIO{$color} . "\n";

    #write to device file
    system("echo \"$ledGPIO{$color}=$oscValue\" > /dev/pi-blaster"); 
}

my $server =
    Net::OpenSoundControl::Server->new(Port => $port, Handler => \&ledAction)
    or die "Could not start server: $@\n";

print "[OSC Server] Receiving messages on port $port\n";

$server->readloop();
print $server->port();
