<?php
?>

<?php
header("refresh: 60");
  
$url = "https://api.openweathermap.org/data/2.5/weather?lat=37.48&lon=-86.29&appid=</appid'/>";
$json = file_get_contents($url);
$json_data = json_decode($json, true);
print_r($json_data);
$temp_k = $json_data[main][temp];
$temp_f = (number_format($temp_k)-273.15)*1.8+32;
$temp_mk = $json_data[main][temp_min];
$temp_mf = (number_format($temp_mk)-273.15)*1.8+32;
$temp_Mk = $json_data[main][temp_max];
$temp_Mf = (number_format($temp_Mk)-273.15)*1.8+32;

  
?>

<!DOCTYPE html>
<html>
<head>
 <title>LOCAL ENVIROMENT</title>
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
<meta http-equiv="Pragma" content="no-cache" />
<meta http-equiv="Expires" content="0" />
<style>
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto;
  gap: 10px;
  background-color: #2196F3;
  padding: 10px;
}

.grid-container > div {
  background-color: rgba(255, 255, 255, 0.8);
  text-align: center;
  padding: 10px 0;
  font-size: 30px;
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

<h1>Office Enviroment</h1>

<p>Tempature and humidity on front porch office:</p>

<div class="grid-container">
  <div class="item1"><?php echo date('D M d Y'); ?><br><?php echo date('H:i:s'); ?> </div>
  <div class="grid-item2">outside temp</div>
  <div class="grid-item3">minium temp</div>
  <div class="grid-item4">max temp</div>  
  <div class="grid-item5"><?php print($temp_f);?></div>
  <div class="grid-item6"><?php print($temp_mf);?></div>
  <div class="grid-item7"><?php print($temp_Mf);?></div> 
   <div class="item8"></div>
  <div class="grid-item9">desk light</div>
  <div class="grid-item10">tv lamp</div>
  <div class="grid-item11">grow light</div> 
 </div>
<div class="footer">
  <p>
<div class="footer_box">weather</div>
<div class="footer_box">Lights</div>
<div class="footer_box">music</div>

</p>
</div>

</body>
</html>


