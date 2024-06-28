<?php 
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "myDBPDO";

	try {
		$conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
		$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

		$sql = "select * from person";

		$stmt = $conn->prepare($sql);
  		$stmt->execute();

  		while($result = $stmt->fetch()) {
  			echo "<h1>{$result['firstname']} {$result['lastname']} {$result['country']} </h1>";
  		}

	
	} catch(PDOException $e) {
		echo $sql . "<br>" . $e->getMessage();
	}
	$conn = null;
?>