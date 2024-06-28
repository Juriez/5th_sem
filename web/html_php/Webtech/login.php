<?php
session_start();
if(isset($_SESSION['username'])) {
    header("Location: dashboard1.php");
    exit();
}

include('db.php');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Fetch user data from the database
        $user = $result->fetch_assoc();
        
        // Set user ID in session
        $_SESSION['user_id'] = $user['id'];
        
        // Set username in session
        $_SESSION['username'] = $username;
        
        // Redirect to dashboard
        header("Location: dashboard1.php");
        exit();
    } else {
        echo "Login failed. Invalid username or password.";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="dashboard1.php">Dashboard</a></li>
            <li><a href="order.php">Order</a></li>
            <li><a href="signup.php">Sign Up</a></li>
            <li><a href="login.php">Login</a></li>
        </ul>
    </nav>
    <div class="container">
        <h2>Login</h2>
        <form action="login.php" method="post">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Login</button>
        </form>
        <a href="signup.php">Sign Up</a>
    </div>
</body>
</html>
