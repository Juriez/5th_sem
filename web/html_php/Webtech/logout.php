<?php
session_start();

// Close the database connection if it's open
include('db.php');
if ($conn->ping()) {
    $conn->close();
}

// Unset all of the session variables
$_SESSION = array();

// Destroy the session cookie
if (ini_get("session.use_cookies")) {
    $params = session_get_cookie_params();
    setcookie(session_name(), '', time() - 42000,
        $params["path"], $params["domain"],
        $params["secure"], $params["httponly"]
    );
}

// Destroy the session
session_destroy();

// Redirect to the login page (you can change the location if needed)
header("Location: login.php");
exit();
?>
