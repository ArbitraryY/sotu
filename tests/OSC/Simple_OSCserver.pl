#!/usr/bin/perl

use strict;
use Net::OpenSoundControl::Server;
my $port = 4567;

use Data::Dumper qw(Dumper);

sub ledAction {
    my $oscMsgRef  = $_[1]; #assign OSC msg reference to var
    my $oscAddress = "@{ $oscMsgRef }[0]";
    my $oscType    = "@{ $oscMsgRef }[1]";
    my $hostname   = "@{ $oscMsgRef }[2]";
    my $status     = "@{ $oscMsgRef }[3]";
    my $value     = "@{ $oscMsgRef }[4]";
    my $status2    = "@{ $oscMsgRef }[5]";
    my $program    = "@{ $oscMsgRef }[6]";
    #print Dumper $oscMsgRef;
    print "-----------------------------\n";
    print "Address:" . "$oscAddress\n" ;
    #print "type:" . "$oscType\n" ;
    print "LED:" . "$hostname\n";
    #print "service:" . "$status\n\n"; 
    print "value:" . "$value\n"; 
    #print "service2:" . "$status2\n\n"; 
    print "program:" . "$program\n\n"; 
}

my $server =
    Net::OpenSoundControl::Server->new(Port => $port, Handler => \&ledAction)
    or die "Could not start server: $@\n";

print "[OSC Server] Receiving messages on port $port\n";

$server->readloop();
print $server->port();
