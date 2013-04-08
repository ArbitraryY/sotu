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
#$client->send(["/ard/red" ,'i', 255,]);

my $mesgVal = 0; #off
#for(;;){
#for (1..1000000) {
#	if ($mesgVal == 0 ) {
# 		$mesgVal = 1;
#       } else {
#		$mesgVal = 0;
#	    }
	$mesg = '/live/play/clip';
	#$client->send(["$mesg" ,'i', 1]);
	$client->send(["/live/play/clip" ,'i', 1, 'i', 1]);
	sleep(5);
	$client->send(["/live/stop" ,'i', 1]);
#}
