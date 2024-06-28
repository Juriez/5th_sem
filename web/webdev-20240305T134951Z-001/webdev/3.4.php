<?php
$servername = "localhost";
$username = "root";
$password = "iit123";
$dbname = "myDB";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$sql =" UPDATE person SET Age = '36'
WHERE FirstName = 'Peter' AND LastName = 'Griffin' "
;

if (mysqli_query($conn, $sql)) {
    echo "Record updated successfully";
} else {
    echo "Error updating record: " . mysqli_error($conn);
}

mysqli_close($conn);
?>

