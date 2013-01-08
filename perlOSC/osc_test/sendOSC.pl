#!C:\xampp\perl\bin\perl.exe
#
use lib 'C:\xampp\perl\lib';
use Net::OpenSoundControl::Client; 

my $port = '';

if (@ARGV != 2) {
	print "\n\tusage: perl sendOSC.pl <server IP> <port#>\n\n";
	exit;
} else {
	$server_ip = $ARGV[0];
	$port = $ARGV[1];
}
my $client = Net::OpenSoundControl::Client->new(
		Host => $server_ip, Port => $port)
		or die "could not start client: $@\n";

#Send test OSC messages
#$client->send(["/ard/s" ,'i', 4, 'i', 5]);
my $mesgVal = 0; #off
for (1..1000000) {
	if ($mesgVal == 1 ) {
		$mesgVal = 100;
	    } else {
		$mesgVal = 1;
	    }
	    $mesg = "/ard/s";
	$client->send(["$mesg" ,'i', $mesgVal]);
	print $mesgVal . "\n";
	#sleep(1);
}
