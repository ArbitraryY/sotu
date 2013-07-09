<?php
error_reporting(E_WARNING);
require_once("lib/OSC.php");

echo "----";
echo $_POST['rVal'];
echo "----";
echo $_POST['gVal'];
echo "----";
echo $_POST['bVal'];
echo "----";
echo $_POST['stripNum'];


#$c = new OSCClient();
#$c->set_destination("127.0.0.1", 10000);
$oscAddress = "/pltn/led"

#$m1 = new OSCMessage("", array("aStringParameter"));
#$m1->add_arg(31337.31337, "f");
#$m1->add_arg(7, "i");
#$m1->add_arg('hello', "s");

#$c->send($m1);


?>

