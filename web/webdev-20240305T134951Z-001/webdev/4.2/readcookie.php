<?php

	if (isset($_COOKIE["Cookie_Name"]))
	{
	  $Value = $_COOKIE["Cookie_Name"];
	  $expire=time()+60*60*24*3;
	  setcookie("Cookie_Name", $Value, $expire);
	  $Value = "The Value of Cookie_Name is " . $Value;
	 }
	else
	{
	  $Value = "Cookie not set";
	}
	echo $Value; 


 ?>
