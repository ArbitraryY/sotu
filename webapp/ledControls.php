<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>PLTN Web Controls</title>
</head>

<body>

<script src="js/jquery-1.8.3.js"></script>
	<script>
                        $( document ).ready(function() {
                                $('#r1').click(function( e ) {
                                        //alert(document.getElementById('r1').name);
                                        e.preventDefault();
                                        e.stopPropagation();
                                        sendOSC();
                                });
                        });
                        function sendOSC() {
                                $.ajax({
                                        type: "POST",
                                        url: "sendOSC.php",
                                        data: {}, stuff to send to PHP function
                                        success: function (response) {
                                                alert ("sent OSC Message");
                                        }
                                });
                        }
        </script>


<?php
$numPis = 6;
$numRGBbuttons = 3;
$RGBButtons = array( 
	"1" => "r",
	"2" => "g",
	"3" => "b",
);
$numStrips = 2;
$hostname = exec('hostname -f');

echo "<h1>$hostname</h1>";

#for ($i = 1; $i <= $numPis; $i++) {
	for ($k = 1 ; $k <= $numStrips ; $k++){
		for ($j = 1; $j <= $numRGBbuttons; $j++){
			echo "";
			echo "<input id=\"$RGBButtons[$j]$k\" name=\"$RGBButtons[$j]$k\" type=\"button\" value=\"$RGBButtons[$j]$k\">";
		}
		echo "<br/><br/><br/>";
	}
#}

?>

</body>
</html>
