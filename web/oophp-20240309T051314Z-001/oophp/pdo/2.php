<?php 
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "myDBPDO";

	try {
		$conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
		$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

		$sql = "create table person (firstname varchar(100), lastname varchar(100), country varchar(100))";

		$conn->exec($sql);
		echo "Table created successfully";

	} catch(PDOException $e) {
		echo $sql . "<br>" . $e->getMessage();
	}
	$conn = null;
?>