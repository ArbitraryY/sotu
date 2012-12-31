#!C:\xampp\perl\bin\perl

use strict;
use lib 'C:\xampp\perl\lib';
#use warnings;
use Net::OpenSoundControl::Server;
my $port = 4567;

use Data::Dumper qw(Dumper);

sub dumpmsg {
    print "[$_[0]] ", Dumper $_[1];
}

my $server =
    Net::OpenSoundControl::Server->new(Port => $port, Handler => \&dumpmsg)
    or die "Could not start server: $@\n";

print "[OSC Server] Receiving messages on port $port\n";

$server->readloop();
print $server->port();
