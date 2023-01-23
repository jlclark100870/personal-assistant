<?php
header("refresh: 120");

$file = "enviro.json";  
$json = json_decode(file_get_contents($file), true);



$url = "https://api.openweathermap.org/data/2.5/weather?lat=37.48&lon=-86.29&appid=472bd080e8719f66f75bf94fe4954e0f";
$json_w = file_get_contents($url);
$json_data = json_decode($json_w, true);


$temp_k = $json_data['main']['temp'];
$temp_f = (number_format($temp_k)-273.15)*1.8+32;
$temp_mk = $json_data['main']['temp_min'];
$temp_mf = (number_format($temp_mk)-273.15)*1.8+32;
$temp_Mk = $json_data['main']['temp_max'];
$temp_Mf = (number_format($temp_Mk)-273.15)*1.8+32;
$cloud =$json_data['weather'][0]['description'];
$out_hum=$json_data['main']['humidity'];
$wind_speed=$json_data['wind']['speed'];



?>

<!DOCTYPE html>
<html>
<head>
 <title>LOCAL ENVIROMENT</title>
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
<meta http-equiv="Pragma" content="no-cache" />
<meta http-equiv="Expires" content="0" />
<style>
body{
    /* Setting default text color, background and a font stack */
    font-size:0.825em;
    color:#666;
    background-color:#fff;
    font-family:Arial, Helvetica, sans-serif;
}
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto;
  gap: 10px;
  background-color: #2196F3;
  padding: 20px;
}

.grid-container > div {
  background-color: rgba(255, 255, 255, 0.8);
  text-align: center;
  padding: 1px 0;
  font-size: 20px;
}

.item1 {
  grid-column-start: 1;
  grid-column-end: 4;
}  
.item8 {
  grid-column-start: 1;
  grid-column-end: 4;


}
  .footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: red;
  color: white;
  text-align: center;
}
.footer_box{
  float: left;
  width:300px;
  border: 1px solid black;
  margin: 10px;
  background-color: black;
  
}
</style>

</head>
<body>

<div class="grid-container">
  <div class="item1"><?php echo date('D M d Y'); ?><br><?php echo date('H:i:s'); ?> </div>
  <div class="item8">inside eviroment</div>
  <div class="grid-item2">upper 'temp'</div>
  <div class="grid-item3">lower 'temp'</div>
  <div class="grid-item4">humidity</div>  
  <div class="grid-item5"><?php print($json['fu']);?></div>
  <div class="grid-item6"><?php print($json['fd']);?></div>
  <div class="grid-item7"><?php print($json['h']);?></div> 
  <div class="item8">outside eviroment</div>
  <div class="grid-item9">outside 'temp'</div>
  <div class="grid-item10">minium 'temp'</div>
  <div class="grid-item11">max 'temp'</div>  
  <div class="grid-item12"><?php print($temp_f);?></div>
  <div class="grid-item13"><?php print($temp_mf);?></div>
  <div class="grid-item14"><?php print($temp_Mf);?></div> 
  <div class="grid-item15">outside description</div>
  <div class="grid-item16">humidity</div>
  <div class="grid-item17">wind speed</div>  
  <div class="grid-item18"><?php print($cloud);?></div>
  <div class="grid-item19"><?php print($out_hum);?></div>
  <div class="grid-item20"><?php print($wind_speed);?></div> 
   <div class="item8"><button id="buttonno"type="button" onclick="location.replace('updatedataset.php?var=no')">Trun off alarm</button> last updated <?php print($json['updated']);?> <button id="buttonyes"type="button" onclick="location.replace('updatedataset.php?var=yes')"> Turn on alarm </button></div>

 
 </div>
 <?php
 $fileds = "dataset.json";  
 $jsonds = json_decode(file_get_contents($fileds), true);
 
 if($jsonds['alarm']=="8:00"){
  print "<script type='text/JavaScript'>document.getElementById('buttonyes').style.background='green'</script>";
}
elseif($jsonds['alarm']=="26:00"){
  print "<script type='text/JavaScript'>document.getElementById('buttonno').style.background='green'</script>";
}
    ?>
</body>
</html>


 