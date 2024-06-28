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

	
	$sql = "select * from person";
	
	$result = $conn->query($sql);

	if($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			echo "<h1> {$row['firstname']}  {$row['lastname']}  {$row['country']} </h1>";
		}
	} else {
		echo "No record found";
	}


	$conn->close();

?>