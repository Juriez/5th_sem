<?php
session_start();
if (!isset($_SESSION['username'])) {
    header("Location: login.php");
    exit();
}

include('db.php');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if user ID is set in the session
    if (!isset($_SESSION['user_id']) || empty($_SESSION['user_id'])) {
        echo "Error: User ID not found in session.";
        exit();
    }

    $user_id = $_SESSION['user_id'];
    $product_name = $_POST['product_name'];
    $quantity = $_POST['quantity'];
    $price = $_POST['price'];

    // Insert order into database
    $sql = "INSERT INTO orders (user_id, product_name, quantity, price) VALUES ('$user_id', '$product_name', '$quantity', '$price')";
    if ($conn->query($sql) === TRUE) {
        echo "Order placed successfully!";
        exit();
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h2>Place Order</h2>
        <form action="order.php" method="post">
            <input type="text" name="product_name" placeholder="Product Name" required><br>
            <input type="number" name="quantity" placeholder="Quantity" required><br>
            <input type="number" name="price" placeholder="Price" required><br>
            <button type="submit">Place Order</button>
        </form>
        <a href="dashboard.php">Back to Dashboard</a>
    </div>
</body>
</html>
