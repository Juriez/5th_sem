<?php
session_start();
$_SESSION['username'] = 'Tom';
if(isset($_SESSION['username'])){
echo 'Welcome ' . $_SESSION ['username'];
}
else{
echo 'You are not logged in!';
}
?>

