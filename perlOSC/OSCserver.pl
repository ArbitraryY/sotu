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
    my $oscAddress =~ m/ard\/(\w+)/;
    print "Color: " . $1 . "\n";
    #hash of colors and corresponding GPIO on RPi
    my %ledGPIO = (
		"red"   => "5", #GPIO 23
		"green" => "2", #     18
		"blue"  => "6", #     24
	       );    
}

my $server =
    Net::OpenSoundControl::Server->new(Port => $port, Handler => \&ledAction)
    or die "Could not start server: $@\n";

print "[OSC Server] Receiving messages on port $port\n";

$server->readloop();
print $server->port();
