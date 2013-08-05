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

my $mesg = "/pltn/heartbeat";
my $hostname = "PLTN1";
my $onOff = "1";
my $pid = "23546";
for(;;){
	#if ($mesgVal == 0 ) {
	#	$mesgVal = 1;
	#} else {
	#	$mesgVal = 0;
	#    }
	#    $mesg = "/ard/red";
	$client->send(["$mesg" ,'s', $hostname,'i',$onOff,'i',$pid]);
	print $mesgVal . "\n";
	sleep(5);
}
