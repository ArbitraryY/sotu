#! c:\perl\bin\perl.exe
##WIN THE LOTTERY WITH PERL!!!

#use Array::Compare;
#use Math::Combinatorics;
use strict;

my $menuchoice = &menu;

if ($menuchoice == 1){
	&generatePicks;
}
elsif ($menuchoice == 2){
	&comparePick;
}
elsif ($menuchoice == 3){
	&generatePicksBasis;
}
elsif ($menuchoice == 4){
	&generatePicksPool;
}
else {
	print "Incorrect menu option\n";
	exit;
}


#####------Sub Functions--------->>>>

#get menu choice
sub menu{
	print "1. Generate Quickpicks\n";
	print "2. Compare a pick\n";
	print "3. Generate Basis Quickpicks\n";
	print "4. Generate Pool Quickpicks\n";
	print "\nWhat would you like to do?:";
	my $choice = <STDIN>;
	return $choice;
}


##This function will generate X number of Mega Millions quickpicks you.
sub generatePicks{
open (PICKS , ">quickpicks.txt");
print "How many quick picks do you want?:";
my $tickets = <STDIN>;
chomp($tickets);
	print "\n";
	print "\n";
print "Here's your $tickets Quick Pick(s)" . "\n\n";

for (my $n=1 ; $n<=$tickets ; $n++){
	my @numbers = ();
	my $mega = '';
	@numbers = &generateNumbers(5,56);
	$mega = &randNum(46);
	push @numbers , ("mega: " . $mega);
	print PICKS $n . ": ";
	print $n . ": ";
	foreach my $number (sort @numbers){
		print PICKS $number . "\t";
		print $number . "\t";
	}
	print PICKS "\n";
	print "\n";
    }
}

sub comparePick{
	print "Enter the quickpick you want to compare (separate by commas):";
	my $pick = <STDIN>;
	chomp($pick);
	my @pick_numbers = split(',',$pick);
	my $compare_result = 0;
	my $iteration_number = 0;
    my $start_time = "";
	#continue to generate a new random array until find a match
	while ($compare_result == 0){	
		my @random_pick = &generateNumbers(6,56);
		$iteration_number++;
		#now compare the arrays.  Need to use the perm method since the 
		#arrays just be simple permutations of one another...i.e they don't 
		#need to be same by digit, just same contents...any order
		my $comp = Array::Compare->new;

  		if ($comp->perm(\@pick_numbers, \@random_pick)) {
            my $end_time = "";
    			foreach my $pick_number (@pick_numbers){
                                print $pick_number . ",";
                        }
                        print "\n";
                        foreach my $random_number (@random_pick){
                                print $random_number . ",";
                        }
			print "Arrays are the same after $iteration_number iteration(s)!\n";
			print "START TIME: $start_time, END TIME: $end_time" . "\n";
			$compare_result = 1;
  		} else {
			foreach my $pick_number (@pick_numbers){
				print $pick_number . ",";
			}
			print "\n";
			foreach my $random_number (@random_pick){
				print $random_number . ",";
			}
    			print "\nArrays are different after $iteration_number iteration(s)!\n";
		}
	}
}
## This function will generate quickpicks based on 

sub generatePicksBasis{
    
    print "Enter the 5 sets of basis vectors (separate by commas) \n\n";
    print "Level 1 (Highest Occurence Rate (OR)):";
    my $level1numbers = <STDIN>;
    chomp($level1numbers);
    my @level1 = split(',', $level1numbers);
    print "Level 2: ";
    my $level2numbers = <STDIN>;
    chomp($level2numbers);
    my @level2 = split(',', $level2numbers);
    print "Level 3: ";
    my $level3numbers = <STDIN>;
    chomp($level3numbers);
    my @level3 = split(',', $level3numbers);
    print "Level 4: ";
    my $level4numbers = <STDIN>;
    chomp($level4numbers);
    my @level4 = split(',', $level4numbers);
    print "Level 5: ";
    my $level5numbers = <STDIN>;
    chomp($level5numbers);
    my @level5 = split(',', $level5numbers);

    print "\n\nEnter the Mega number basis vector (separate by commas):";
    my $meganumbers = <STDIN>;
    chomp($meganumbers);
    my @mega = split(',', $meganumbers);
    
    print "\n\nHow many picks do you want from this basis???:";
    my $number_of_picks = <STDIN>;
    chomp($number_of_picks);


    ##Determine array sizes for parsing
    my $level1size = scalar @level1;
    my $level2size = scalar @level2;
    my $level3size = scalar @level3;
    my $level4size = scalar @level4;
    my $level5size = scalar @level5;
    my $megasize   = scalar @mega;
    
    ## Determine the number of possible sets of lottery numbers 
    ## (permutations) based on these array entries
    my $n = $level1size + $level2size + $level3size + $level4size + $level5size + $megasize;
    my $k = 6;
    print "n =" . $n;
    print "k =" . $k;
    print "--------------------------------------------------\n";
    print "The number of possible lottery numbers is:" . factorial($n) / factorial($n - $k);
    print "-------------------------------------------------\n";
    system(pause);
    
    
    ## push these into hashes
    my %level1 = ();
    my %level2 = ();
    my %level3 = ();
    my %level4 = ();
    my %level5 = ();
    my %mega   = ();
    
    my $size = 0;
    foreach my $number (@level1){
        $level1{$size} = $number;
        $size++;        
    }
    my $size = 0;
    foreach my $number (@level2){
        $level2{$size} = $number;
        $size++;        
    }
    my $size = 0;
    foreach my $number (@level3){
        $level3{$size} = $number;
        $size++;        
    }
    my $size = 0;
    foreach my $number (@level3){
        $level3{$size} = $number;
        $size++;        
    }
    my $size = 0;
    foreach my $number (@level4){
        $level4{$size} = $number;
        $size++;        
    }
    my $size = 0;
    foreach my $number (@level5){
        $level5{$size} = $number;
        $size++;        
    }
    my $size = 0;
    foreach my $number (@mega){
        $mega{$size} = $number;
        $size++;        
    }
    open(PICKS,">c:\\perl\\lottery\\data\\picks\\picks.txt");
    for (my $j = 0 ; $j <= $number_of_picks ; $j++){
        ##Generate a random number to pick one of the elements of each hash
        my $level1pickkey = &randNumFromZero($level1size);
        my $level2pickkey = &randNumFromZero($level2size);
        my $level3pickkey = &randNumFromZero($level3size);
        my $level4pickkey = &randNumFromZero($level4size);
        my $level5pickkey = &randNumFromZero($level5size);
        my $megapickkey   = &randNumFromZero($megasize);

    
        ##Print out the number for that pick from the hash
        my @pick = ($level1{$level1pickkey},$level2{$level2pickkey},$level3{$level3pickkey},$level4{$level4pickkey},$level5{$level5pickkey},$mega{$megapickkey});

        print PICKS $j + 1 .": ";
        foreach my $pick_number (@pick){
            print $pick_number . "\t";
            print PICKS $pick_number . "\t";
        }
        print "\n\n\n";
        print PICKS "\n\n\n";
    }
    
}##End generatePicksBasis

## This function generates X number of picks based on a given pool of numbers   
sub generatePicksPool{
    print "Enter the pool of numbers (separate by commas) \n\n";
    my $main_numbers = <STDIN>;
    chomp($main_numbers);
    my @main_numbers = split(',', $main_numbers);

    print "Enter the pool of mega numbers (separate by commas) \n\n";
    my $mega_numbers = <STDIN>;
    chomp($mega_numbers);
    my @mega_numbers = split(',', $mega_numbers);

    print "\n\nHow many picks do you want from this pool???:";
    my $number_of_picks = <STDIN>;
    chomp($number_of_picks);

    my %main_numbers_hash = ();
    my %mega_numbers_hash = ();

    ##Determine size of arrays
    my $main_numbers_size = scalar @main_numbers;
    my $mega_numbers_size = scalar @mega_numbers;
    
    ## Now put numbers into a hash
    my $size = 0;
    foreach my $main_number (@main_numbers){
        $main_numbers_hash{$size} = $main_number ;
        $size++;
    }
    my $size = 0;
    foreach my $mega_number (@mega_numbers){
        $mega_numbers_hash{$size} = $mega_number ;
        $size++;        
    }
    open(PICKS,">c:\\perl\\lottery\\data\\picks\\picks_pool.txt");
    
    for (my $j = 0 ; $j <= $number_of_picks ; $j++){
        my @pick_array = ();
        ##Generate a random number to pick one of the elements of each hash
        for (my $i = 1 ; $i <= 5 ; $i++){ 
            my $main_number_key = &randNumFromZero($main_numbers_size);
            push @pick_array , $main_numbers_hash{$main_number_key};
        }
        my $mega_number_key = &randNumFromZero($mega_numbers_size);
        push @pick_array , "mega: " . $mega_numbers_hash{$mega_number_key};
        
        foreach my $pick_array_number (@pick_array){
            print PICKS "$pick_array_number" . "\t";
        }
        print PICKS "\n";
    }


    

}##End generatePicksPool


#Calculate the main numbers, need to pass as first arguement # of 
#numbers you want to generate and the MAX of the range
sub generateNumbers{
	my $amount = $_[0];
	my $range = $_[1];
    my $num = '';
	my @numbers = ();
		for (my $i=1;$i<=$amount;$i++){
			my $times = &randNum(10000); #&randNum(1000000);
			for(my $j=1;$j<=$times;$j++){
				$num = &randNum($range);
			}
		push @numbers , ($num);
		}
	return @numbers;
}

#generate a random number between 1 and MAX
sub randNum{
	my $max = $_[0];
	my $num = 1 + int (rand $max);
	return $num;
}

#generates a random number between 0 and MAX
sub randNumFromZero{
	my $x = $_[0];
    my $iter = 100000;
    my $num = 0;
    for (my $j = 0 ; $j <= $iter ; $j++){
	    $num = int (rand $x);
    }
    return $num;
}
