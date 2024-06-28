<?php

	$host="localhost"; // Host name 
	$username="root"; // Mysql username 
	$password="iit123"; // Mysql password 
	$db_name="test"; // Database name 
	$tbl_name="members"; // Table name 
	// Connect to server and select databse.
	$conn = mysqli_connect($host, $username, $password, $db_name); 
	if (!$conn) {
    	die("Connection failed: " . mysqli_connect_error());
	}
	// username and password sent from form 
	$myusername=$_POST['myusername']; 
	$mypassword=$_POST['mypassword']; 
	// To protect MySQL injection (more detail about MySQL injection)
	$myusername = stripslashes($myusername);
	$mypassword = stripslashes($mypassword);
	$myusername = mysqli_real_escape_string($conn, $myusername);
	$mypassword = mysqli_real_escape_string($conn, $mypassword);
	$sql="SELECT * FROM $tbl_name WHERE username='$myusername' and password='$mypassword'";
	$result=mysqli_query($conn, $sql);
	// Mysql_num_row is counting table row
	$count=mysqli_num_rows($result);
	
	
	// If result matched $myusername and $mypassword, table row must be 1 row
	if($count==1){

	// Register $myusername, $mypassword and redirect to file "login_success.php"
	session_start();
	$_SESSION['myusername'] = $myusername;
	$_SESSION['mypassword'] = $mypassword;
	header("location:login_success.php");
	}
	else {
	echo "Wrong Username or Password";
	}
?>

