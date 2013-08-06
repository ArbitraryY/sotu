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

my $mesg = "/pltn/heartbeat";
my $hostname = "PLTN1";
my $serviceName = "oscServer";
my $onOff = "1";
my $pid = "23546";
my $i = 0;
for(;;){
	print $mesg . " " . $hostname . " " . $i . "\n";
	$client->send(["$mesg" ,'s', $hostname." ".$i, 's', "$serviceName", 'i',$onOff,'i',$pid+$i]);
	sleep(5);
	$i++;
}
