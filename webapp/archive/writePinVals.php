<?php 

/* Configuration area. Will move to .ini file if needed */
$dataDir  = 'data/';
$dataFile = 'pinVals.txt';
/* End of configuration area */

/* Check for pinValue, value checking (numbers onlye) and set to NULL if not present 
 * TODO: Restrict pin values to a set of allowed values. Instead of all Real values :)
 */
$pinValue = ($_POST['pinValue'] && preg_match('/^\d+$/', $_POST['pinValue'])) ? $_POST['pinValue'] : NULL;

$result  = 0;  /* result boolean */
$message = ''; /* human readble message. Mainly for errors */
if ($pinValue == NULL) {
	$result  = 0;
	$message = "In-valid pin value";
}
else {
	/* Make sure the data directory exists before
	 * trying to write to it. Setting permissions to
	 * the web server user */
	if (is_dir($dataDir) == FALSE) {
		mkdir($dataDir, 0700);
	}
	
	/* Write the pin value to the $dataFile */
	file_put_contents("$dataDir$dataFile", "5=$pinValue");
	$result  = 1;
	$message = 'Success';

}

echo '{"result":'.$result.',"msg": "'.$message.'"}';
?>
