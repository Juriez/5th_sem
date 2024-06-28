<?php 
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "myDB";

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) {
	  die("Connection failed: " . $conn->connect_error);
	}

	$sql = "CREATE TABLE person (firstname varchar(100), lastname varchar(100), country varchar(100))";
	if ($conn->query($sql) === TRUE) {
	  echo "Table created successfully";
	} else {
	  echo "Error creating Table: " . $conn->error;
	}
	$conn->close();

?>