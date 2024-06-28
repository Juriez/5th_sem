<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "Student";

$conn = mysqli_connect($servername, $username, $password, $database);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}


$sql_create_table = "
CREATE TABLE IF NOT EXISTS users (
    userid INT AUTO_INCREMENT PRIMARY KEY,
    passid VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    zip VARCHAR(10) NOT NULL,
    email VARCHAR(255) NOT NULL,
    sex VARCHAR(10),
    language VARCHAR(255),
    description TEXT
)";

if (mysqli_query($conn, $sql_create_table)) {
    echo "Table 'users' created successfully.<br>";
} else {
    echo "Error creating table: " . mysqli_error($conn) . "<br>";
}
?>
