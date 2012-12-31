#!C:\xampp\perl\bin\perl.exe
#
use lib 'C:\xampp\perl\lib';
use Net::OpenSoundControl::Client; 

print "Sending msg '/Main/Volume', 'f', $_ / 100";
my $port = "9999";
my $host = "192.168.1.177";
my $client = Net::OpenSoundControl::Client->new(
		Host => $host, Port => $port)
		or die "could not start client: $@\n";

for (0..100) {
	print "Sending msg '/Main/Volume', 'f', $_ / 100";
	$client->send(['/Main/Volume', 'f', $_ / 100]);
	sleep(1);	
}
