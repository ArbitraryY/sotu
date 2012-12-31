#!C:\xampp\perl\bin\perl.exe
#
use lib 'C:\xampp\perl\lib';
use Net::OpenSoundControl::Client; 
use Net::OpenSoundControl::Server;
use Data::Dumper qw(Dumper);

##==== BASIC STUFF ================================       
#require "subparseform.lib";
&Parse_Form;
$message = $formdata{'message'};
print "Content-type: text/html\n\n";
print "OSC Client: Sending out messages to localhost\n\n"; 
print "You send the message: $message \n\n";


##===== CLIENT ==================================
my $client = Net::OpenSoundControl::Client->new(Host => "127.0.0.1", Port => 4567);

$client->send([$message]); 


## ========= Sub Routines ========================
sub Parse_Form {
	if ($ENV{'REQUEST_METHOD'} eq 'GET') {
		@pairs = split(/&/, $ENV{'QUERY_STRING'});
	} elsif ($ENV{'REQUEST_METHOD'} eq 'POST') {
		read (STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
		@pairs = split(/&/, $buffer);
		if ($ENV{'QUERY_STRING'}) {
			@getpairs =split(/&/, $ENV{'QUERY_STRING'});
			push(@pairs,@getpairs);
			}
	} else {
		print "Content-type: text/html\n\n";
		print "<P>Use Post or Get";
	}
	foreach $pair (@pairs) {
		($key, $value) = split (/=/, $pair);
		$key =~ tr/+/ /;
		$key =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$value =~s/<!--(.|\n)*-->//g;

		if ($formdata{$key}) {
			$formdata{$key} .= ", $value";
		} else {
			$formdata{$key} = $value;
		}
	}
}	
1;





