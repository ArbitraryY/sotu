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

#connect to PDE OSC Server
#$client->send(['/server/connect']);

#Send test OSC messages
for (0..100) {
	if ($color eq 'red') {
		$color = 'blue';
	    } elsif ($color eq 'blue') {
		$color = 'green';
	    } else {
		$color = 'red';
	    }
	    $mesg = "/ard/test2";
	$client->send(["$mesg" ,'i', 255]);
	#$client->send(["$mesg2", 'f', $_ / 150]);
	#print "/Main/Volume f $_ / 100 ";
	print "$mesg\n";
	sleep(1);
}
#disconnect from PDE OSC server
#$client->send(['/server/disconnect']);
