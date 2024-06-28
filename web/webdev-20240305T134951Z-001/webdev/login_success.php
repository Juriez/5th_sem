
<?php
// Check if session is not registered, redirect back to main page. 
// Put this code in first line of web page. 
	if(isset($_SESSION['myusername']) && isset($_SESSION['mypassword'])){
		echo 'Login Successful';
	} 
	else {
		header("location:main_login.php");
	}
?>

