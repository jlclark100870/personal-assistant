<?php
$file = "dataset.json";  
$json = json_decode(file_get_contents($file), true);
$upper_temp = $json['upper_temp'];
$lower_temp = $json['lower_temp'];
if ($_GET["var"]=="yes"){
	$alarm="8:00";
}elseif($_GET["var"]=="no"){
	$alarm="26:00";
}	

$dataset = array("upper_temp"=>$upper_temp, "lower_temp"=>$lower_temp, "alarm"=>$alarm);
file_put_contents('dataset.json', json_encode($dataset));
header('Location: index.php');
?>