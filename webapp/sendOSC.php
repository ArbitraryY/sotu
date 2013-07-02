<?php
error_reporting(E_WARNING);
require_once("lib/OSC.php");

echo "<h1>sent</h1>";
$testVar = 37;
$testVar2 = 19;

echo '{"result":' . $testVar . ',"msg": "' . $testVar2 . '"}';

$c = new OSCClient();
$c->set_destination("127.0.0.1", 10000);

$m1 = new OSCMessage("/test", array("aStringParameter"));
$m1->add_arg(31337.31337, "f");
$m1->add_arg(7, "i");
$m1->add_arg('hello', "s");

$c->send($m1);


?>

