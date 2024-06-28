<?php
include 'database_connection.php';


function getUserRows($result) {
    $rows = "";
    while ($row = mysqli_fetch_assoc($result)) {
        $rows .= "<tr>";
        $rows .= "<td>".$row["userid"]."</td>";
        $rows .= "<td>".$row["passid"]."</td>";
        $rows .= "<td>".$row["username"]."</td>";
        $rows .= "<td>".$row["address"]."</td>";
        $rows .= "<td>".$row["country"]."</td>";
        $rows .= "<td>".$row["zip"]."</td>";
        $rows .= "<td>".$row["email"]."</td>";
        $rows .= "<td>".$row["sex"]."</td>";
        $rows .= "<td>".$row["language"]."</td>";
        $rows .= "<td>".$row["description"]."</td>";
        $rows .= "</tr>";
    }
    return $rows;
}


if ($_SERVER["REQUEST_METHOD"] == "POST") {
  
    $userid = $_POST["userid"];
    $passid = $_POST["passid"];
    $username = $_POST["username"];
    $address = $_POST["address"];
    $country = $_POST["country"];
    $zip = $_POST["zip"];
    $email = $_POST["email"];
    $sex = isset($_POST["sex"]) ? $_POST["sex"] : "";
    $language = isset($_POST["en"]) ? "English" : "";
    $language .= isset($_POST["nonen"]) ? ", Non English" : "";
    $description = $_POST["desc"];

   
    $userid = mysqli_real_escape_string($conn, $userid);
    $passid = mysqli_real_escape_string($conn, $passid);
    $username = mysqli_real_escape_string($conn, $username);
    $address = mysqli_real_escape_string($conn, $address);
    $country = mysqli_real_escape_string($conn, $country);
    $zip = mysqli_real_escape_string($conn, $zip);
    $email = mysqli_real_escape_string($conn, $email);
    $sex = mysqli_real_escape_string($conn, $sex);
    $language = mysqli_real_escape_string($conn, $language);
    $description = mysqli_real_escape_string($conn, $description);

 
    $sql = "INSERT INTO users (userid, passid, username, address, country, zip, email, sex, language, description)
            VALUES ('$userid', '$passid', '$username', '$address', '$country', '$zip', '$email', '$sex', '$language', '$description')";

   
    if (mysqli_query($conn, $sql)) {
        echo "New record Added successfully";
    } else {
        echo "Error: Unable to execute query " . mysqli_error($conn);
    }
}

$sql_select = "SELECT * FROM users";
$result = mysqli_query($conn, $sql_select);


$tableRows = getUserRows($result);

mysqli_close($conn);
?>

<table id="tblData" style="width: 100%; border-collapse: collapse;">
    <tr>
        <th style="background-color: #f2f2f2; text-align: left; padding: 8px;">User ID</th>
        <th style="background-color: #f2f2f2; text-align: left; padding: 8px;">Password</th>
        <th style="background-color: #f2f2f2; text-align: left; padding: 8px;">Name</th>
        <th style="background-color: #f2f2f2; text-align: left; padding: 8px;">Address</th>
        <th style="background-color: #f2f2f2; text-align: left; padding: 8px;">Country</th>
        <th style="background-color: #f2f2f2; text-align: left; padding: 8px;">ZIP Code</th>
        <th style="background-color: #f2f2f2; text-align: left; padding: 8px;">Email</th>
        <th style="background-color: #f2f2f2; text-align: left; padding: 8px;">Sex</th>
        <th style="background-color: #f2f2f2; text-align: left; padding: 8px;">Language</th>
        <th style="background-color: #f2f2f2; text-align: left; padding: 8px;">Description</th>
    </tr>
    <?php echo $tableRows; ?>
</table>

