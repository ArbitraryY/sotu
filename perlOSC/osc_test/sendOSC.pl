#!C:\xampp\perl\bin\perl.exe
#
use lib 'C:\xampp\perl\lib';
use Net::OpenSoundControl::Client; 

my $port = '';

if (@ARGV != 1) {
	print "\n\tusage: perl sendOSC.pl <port#>\n\n";
	exit;
} else {
	$port = $ARGV[0];
}
my $client = Net::OpenSoundControl::Client->new(
		Host => "127.0.0.1", Port => $port)
		or die "could not start client: $@\n";

#connect to PDE OSC Server
#$client->send(['/server/connect']);

#Send test OSC messages
$color = 'red';
for (0..100) {
	$OSC_color = '';
	#$client->send(['/layer1/pos_x', 'f', $_ / 30]);
	#$client->send(['/layer1/fade', 'f', $_ /30]);
	if ($color eq 'red') {
		$color = 'blue';
	    } elsif ($color eq 'blue') {
		$color = 'green';
	    } else {
		$color = 'red';
	    }
	    $mesg = "/layer1/pos_x";
	    $mesg2 = "/layer1/pos_y";
	$client->send(["$mesg", 'f', $_ / 150]);
	$client->send(["$mesg2", 'f', $_ / 150]);
	#print "/Main/Volume f $_ / 100 ";
	print "message $_; Message is $mesg($_ / 10),$mesg2($_ / 30 ) \n";
	sleep(1);
}
#disconnect from PDE OSC server
#$client->send(['/server/disconnect']);
