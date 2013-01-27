#! C:\perl\bin\perl.exe

use XML::Simple;
use Data::Dumper;

#my $lotterydata = "c:\\perl\\lottery\\data\\lotterydata.txt";
my $lotterydata = "c:\\perl\\lottery\\data\\megamillions.txt";
#my $xmlfile = "c:\\perl\\lottery\\data\\lotterydata.xml";
my $xmlfile = "c:\\perl\\lottery\\data\\megamillions.xml";
my $xs = XML::Simple->new();


$fh = open("FH", $lotterydata);

my @numbers = <FH>;

#print Dumper(\@numbers);

#$instuff = $xs->XMLin('c:\perl\data\lotterydata.xml');
#print Dumper($instuff);

my $numbers_hashref = {};

foreach $number (@numbers){
    chomp($number);
    #$number =~ /(\D+)\s(\d+)\/(\d+)\/(\d+)\s(\d+)\-(\d+)\-(\d+)\-(\d+)\-(\d+)\-(\d+)/;
    $number =~ /(\d+)-(\d+)-(\d+),(\d+),(\d+),(\d+),(\d+),(\d+),(\d+)/;
    #print $number . "\n";
=pod
    push @{$numbers_hashref->{'lotto_number'}} , {
                    'weekday' => $1,
                    'month'   => $2,
                    'day'     => $3,
                    'year'    => $4,
                    'one'     => $5,
                    'two'     => $6,
                    'three'   => $7,
                    'four'    => $8,
                    'five'    => $9,
                    'six'     => $10,
            };
=cut
        push @{$numbers_hashref->{'lotto_number'}} , {
                    'month' => $1,
                    'day'   => $2,
                    'year'  => $3,
                    'one'   => $4,
                    'two'   => $5,
                    'three' => $6,
                    'four'  => $7,
                    'five'  => $8,
                    'six'   => $9,
            };
}
print Dumper($numbers_hashref);
$xs->XMLout($numbers_hashref, OutputFile => $xmlfile, NoAttr=>1, RootName=>'numbers');

=pod
$1 = Weekday
$2 = Month
$3 = Day
$4 = Year
##########Digits###########
$5 = One 
$6 = Two
$7 = Three
$8 = Four
$9 = Five
$10 = Six (Mega)
=cut


