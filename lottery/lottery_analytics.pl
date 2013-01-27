#! C:\perl\bin\perl.exe

use XML::Simple;
use Data::Dumper;

my $lotterydata = "c:\\perl\\lottery\\data\\lotterydata.xml";
my $xs = XML::Simple->new();
my @lottery_number_possibilities = (1 .. 47); #super lotto plus
my @mega_number_possibilities = (1 .. 27); #super lotto plus
my @lottery_number_digits = qw(one two three four five);
my $mega_number_digit = 'six';



$fh = open("FH", $lotterydata);
$fh = open("HISTOGRAM", ">c:\\perl\\lottery\\data\\histograms\\histogram_all.csv");
$fh = open("HISTOGRAMMEGA", ">c:\\perl\\lottery\\data\\histograms\\mega_histogram_all.csv");

$xml_lottery_numbers = $xs->XMLin('c:\perl\lottery\data\lotterydata.xml');

my %digit_occurences_hash = {};
my %mega_digit_occurences_hash = {};


#print Dumper($xml_lottery_numbers);

my $occurences = 0;
my $mega_occurences = 0;


foreach $lottery_number (@{$xml_lottery_numbers->{'lotto_number'}}){
    foreach $possibility (@lottery_number_possibilities){
        foreach $digit (@lottery_number_digits){
            if ($lottery_number->{$digit} == $possibility){
                #get the existing value in the hash
                $occurences = $digit_occurences_hash{$possibility};
                #add one to existing value
                $digit_occurences_hash{$possibility} = $occurences + 1;
                last; #if find a match, don't search the remainder of the digits 
                #since same number can't show up twice.
                
            }
        
        }            
    }
    foreach $mega_possibility (@mega_number_possibilities){
            if ($lottery_number->{$mega_number_digit} == $mega_possibility){
                #get the existing value in the hash
                $mega_occurences = $mega_digit_occurences_hash{$mega_possibility};
                #add one to existing value
                $mega_digit_occurences_hash{$mega_possibility} = $mega_occurences + 1;
                last; #if find a match, don't search the remainder of the digits 
                #since same number can't show up twice.
        }           
    }
}
$total = 0;
foreach $temp (keys %digit_occurences_hash){
    print HISTOGRAM "$temp,$digit_occurences_hash{$temp}" . "\n";
    $total = $total +  $digit_occurences_hash{$temp};
}
foreach $mega_temp (keys %mega_digit_occurences_hash){
    print HISTOGRAMMEGA "$mega_temp,$mega_digit_occurences_hash{$mega_temp}" . "\n";
    $mega_total = $mega_total +  $mega_digit_occurences_hash{$mega_temp};
}
print "The Total is:" . ($total + $mega_total) . "\n";

#print Dumper(\%mega_digit_occurences_hash);





####################get data by month and weekday##############################
my @months = (1 .. 12);
my %digit_occurences_months_hash = {};
my $mega_digit_occurences_months_hash = {};
$mega_possibility = 0;
$possibility = 0;
$mega_occurences = 0;
#####$fh = open("BYMONTHHISTOGRAM", ">c:\\perl\\lottery\\data\\histograms\\by_month_weekday_histogram.csv");
$fh = open("BYMONTHHISTOGRAM", ">c:\\perl\\lottery\\data\\histograms\\by_month_histogram.csv");
#####$fhmega = open("BYMONTHHISTOGRAMMEGA", ">c:\\perl\\lottery\\data\\histograms\\by_month_weekday_histogram_mega.csv");
$fhmega = open("BYMONTHHISTOGRAMMEGA", ">c:\\perl\\lottery\\data\\histograms\\by_month_histogram_mega.csv");

foreach $lottery_number (@{$xml_lottery_numbers->{'lotto_number'}}){
    foreach $month (@months){
        $weekday = $lottery_number->{'weekday'}; #gets the weekday of this number occurence, just comment out if want monthly histograms
        %digit_occurences_hash = {};
        if($lottery_number->{'month'} == $month){
            foreach $possibility (@lottery_number_possibilities){
                #check 5 regular numbers
                foreach $digit (@lottery_number_digits){
                    if ($lottery_number->{$digit} == $possibility){
                        #get the existing value in the hash
                        #####$occurences = $digit_occurences_months_hash{$month.",".$weekday}{$possibility};
                        $occurences = $digit_occurences_months_hash{$month}{$possibility};
                        #add one to existing value
                        #####$digit_occurences_months_hash{$month.",".$weekday}{$possibility} = $occurences + 1;
                        $digit_occurences_months_hash{$month}{$possibility} = $occurences + 1;
                        last; #if find a match, don't search the remainder of the digits 
                        #since same number can't show up twice.
                    }
               }
            }
            #check and record mega numbers
            foreach $mega_possibility (@mega_number_possibilities){
                if ($lottery_number->{$mega_number_digit} == $mega_possibility){
                    #get the existing value in the hash
                    #####$mega_occurences = $mega_digit_occurences_months_hash{$month.",".$weekday}{$mega_possibility};
                    $mega_occurences = $mega_digit_occurences_months_hash{$month}{$mega_possibility};
                    #add one to existing value
                    #####$mega_digit_occurences_months_hash{$month.",".$weekday}{$mega_possibility} = $mega_occurences + 1;
                    $mega_digit_occurences_months_hash{$month}{$mega_possibility} = $mega_occurences + 1;
                    last; #if find a match, don't search the remainder of the digits 
                    #since same number can't show up twice.
                }
            }

        }            
    }
}
foreach $month_hist (keys %digit_occurences_months_hash){
    foreach $possibility (@lottery_number_possibilities){
       print BYMONTHHISTOGRAM "$month_hist,$possibility,$digit_occurences_months_hash{$month_hist}{$possibility}" . "\n";
    }
}
foreach $mega_month_hist (keys %mega_digit_occurences_months_hash){
    foreach $mega_possibility (@mega_number_possibilities){
       print BYMONTHHISTOGRAMMEGA "$mega_month_hist,$mega_possibility,$mega_digit_occurences_months_hash{$mega_month_hist}{$mega_possibility}" . "\n";
    }
}
#print Dumper(\%digit_occurences_months_hash);
#print Dumper(\%mega_digit_occurences_months_hash);
