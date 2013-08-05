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
   
}

my $server =
    Net::OpenSoundControl::Server->new(Port => $port, Handler => \&ledAction)
    or die "Could not start server: $@\n";

print "[OSC Server] Receiving messages on port $port\n";

$server->readloop();
print $server->port();
