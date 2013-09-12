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

#my $mesg = "/pltn/led";
my $mesg = "/layer3/clip2/connect";
my $mesg2 = "/layer2/clip2/connect";
my $i = 0;
for(;;){
	print $mesg . " " . $hostname . " " . $i . "\n";
	#$client->send(["$mesg" , 's', "r1", 'i', 1, 's', "flashFade"]);
	#$client->send(["$mesg" , 's', "r2", 'i', 1, 's', "flashFade"]);
	$client->send(["$mesg" , 'i' , 1]);
	sleep(5);
	$client->send(["$mesg2" , 'i' , 1]);
#	$client->send(["$mesg" , 's', "g1", 'i', 0, 's', "solid"]);
#	$client->send(["$mesg" , 's', "g2", 'i', 0, 's', "solid"]);
	$i++;
}
