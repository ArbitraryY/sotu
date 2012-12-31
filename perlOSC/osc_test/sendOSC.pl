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
my $mesgVal = 0; #off
for (0..100) {
	if ($mesgVal == 0 ) {
		$mesgVal = 255;
	    } else {
		$mesgVal = 0;
	    }
	    $mesg = "/ard/test2";
	$client->send(["$mesg" ,'i', $mesgVal]);
	print $mesgVal . "\n";
	sleep(1);
}
