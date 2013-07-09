<?php
error_reporting(E_WARNING);
require_once("lib/OSC.php");

echo "----";
echo $_POST['rVal'];
$rVal = $_POST['rVal'];
echo "----";
echo $_POST['gVal'];
$gVal = $_POST['gVal'];
echo "----";
echo $_POST['bVal'];
$bVal = $_POST['bVal'];
echo "----";
echo $_POST['stripNum'];

#scale for pi-blaster
$rVal =$rVal / 255;
$gVal =$gVal / 255;
$bVal =$bVal / 255;

$rStrip = "r" . $_POST['stripNum'];
$gStrip = "g" . $_POST['stripNum'];
$bStrip = "b" . $_POST['stripNum'];

echo $bStrip;

$c = new OSCClient();
$c->set_destination("127.0.0.1", 4567);
$oscAddress = "/pltn/led";

$r = new OSCMessage($oscAddress, array($rStrip, $rVal, "solid"));
$g = new OSCMessage($oscAddress, array($gStrip, $gVal, "solid"));
$b = new OSCMessage($oscAddress, array($bStrip, $bVal, "solid"));
#$m1->add_arg(31337.31337, "f");
#$m1->add_arg(7, "i");
#$m1->add_arg('hello', "s");

$c->send($r);
$c->send($g);
$c->send($b);


?>

