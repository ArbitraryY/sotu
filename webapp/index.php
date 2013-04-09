<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Demo</title>
</head>
<body>
	<script src="js/jquery.js"></script>
		<script>
			$( document ).ready(function() {
				$('#rLEDbutton').click(function( e ) {
					//alert(document.getElementById('LEDbutton').name);
					e.preventDefault();
					e.stopPropagation();
					setColor();
				});
			});
			function setColor() {
				$.ajax({
					type: "POST",
					url: "writePinVals.php",
					//data: {}, stuff to send to PHP function
					success: function (response) {
						alert ("sent pin values");
					}
				});
			}
		</script>

<input id="rLEDbutton" name="rLED" type="button" value="red" />
<input id="gLEDbutton" name="gLED" type="button" value="green" />
<input id="bLEDbutton" name="bLED" type="button" value="blue" />

</body>
</html>