<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>jQuery UI Slider - Multiple sliders</title>
<!--<link rel="stylesheet" href="http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css" />-->
<script src="js/jquery-1.9.1.js"></script>
<script src="js/jquery-ui-1.10.3.js"></script>
<!--<link rel="stylesheet" href="/resources/demos/style.css" />-->
<link rel="stylesheet" href="css/jquery-ui-1.10.3.css" />
<style>
	#sliders span {height:120px; float:left; margin:15px}
</style>
<script>
	 function hexFromRGB(r, g, b) {
		var hex = [
			r.toString( 16 ),
			g.toString( 16 ),
			b.toString( 16 )
		];
		$.each( hex, function( nr, val ) {
		if ( val.length === 1 ) {
			hex[ nr ] = "0" + val;
			}
		});
		return hex.join( "" ).toUpperCase();
	}
	$(function() {
	// setup RGB Sliders
		$( "#sliders > span" ).each(function() {
			// read initial values from markup and remove that
			var value = parseInt( $( this ).text(), 10 );
			$( this ).empty().slider({
				value: value,
				range: "min",
				max: 255,
				animate: true,
				orientation: "vertical",
				change: updateRGBVals,
				slide: updateRGBVals
			});
		});
	});
	function updateRGBVals() {
		//Change the LED value	
		var colorVal = $( this ).slider("value");
		var slider_id = this.id;
		//alert (strip_num[1]);
		//Build the ID of the slider
		var html_slider_id = "#val_" + slider_id;
		//update the value on the screen
		$( html_slider_id ).html(colorVal);
		//Update the swatch
		var strip_num = slider_id.match(/(\d+)/);
		var r_strip_id = "#slider_r"+strip_num[1]; 
		var g_strip_id = "#slider_g"+strip_num[1]; 
		var b_strip_id = "#slider_b"+strip_num[1];
		//alert( r_strip_id )
		var swatch = "#strip"+strip_num[1];
		var r = $( r_strip_id ).slider("value"),
		    g = $( g_strip_id ).slider("value"),
		    b = $( b_strip_id ).slider("value"),
		    hex = hexFromRGB( r,g,b );
		//alert (swatch)
		$( swatch ).css("background-color", "#" + hex);
		sendOSC(r,g,b,strip_num[1]);
		// Ajax Code to send updates to sendOSC.php goes here
	}
	function sendOSC(r,g,b,strip_num){
		$.ajax({
                	type: "POST",
			url: "sendOSC.php",
                        data: {rVal: r, gVal: g, bVal: b, stripNum: strip_num}, //stuff to send to PHP function
                        success: function (response) {
				//alert(response);
                        	//alert ("sent OSC Message");
                        	}
       		});
	}		

	 $(function() {
		$( "button" )
			.button()
			.click(function( event ) {
				event.preventDefault();
			});
	});
</script>
</head>
<body style="font-family: Courier New;">

<?php
$hostname = exec('hostname -f');

echo "<h1>$hostname</h1>";

$numLEDStrips = 2;

$buttons = array(
	"1" => "r",
	"2" => "g",
	"3" => "b",
);
for ($strip=1 ; $strip <=$numLEDStrips ; $strip++){ 
	echo "<div id=\"strip$strip\" style=\"width:100px; height:100px; border:1px solid #999;\"></div>";
	for($i=1 ; $i <=sizeof($buttons) ; $i++){
		echo "<button id=\"$buttons[$i]$strip\">$buttons[$i]$strip</button>";
	};
	echo "&nbsp;&nbsp;&nbsp;";
};
echo "&nbsp;&nbsp;&nbsp;";
echo "<div id=\"sliders\">";
for ($strip=1 ; $strip <=$numLEDStrips ; $strip++){ 
	for($i=1 ; $i <=sizeof($buttons) ; $i++){
		echo "<span id=\"slider_$buttons[$i]$strip\">0</span>";
		echo "<div id=\"val_slider_$buttons[$i]$strip\">0</div>";
	};
};
echo "</div>";
	
?>

</body>
</html>

