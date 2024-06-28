<?php 
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "myDBPDO";

	try {
		$conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
		$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

		$sql = "insert into person (firstname, lastname, country) values ('James', 'Bond', 'UK')";

		$conn->exec($sql);
		echo "Data inserted successfully";

	} catch(PDOException $e) {
		echo $sql . "<br>" . $e->getMessage();
	}
	$conn = null;
?>