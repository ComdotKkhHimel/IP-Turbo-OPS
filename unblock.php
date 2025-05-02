<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $ip = trim($_POST["ip"]);

    if (filter_var($ip, FILTER_VALIDATE_IP)) {
        // Simulate unblocking the IP (in real use, you would use firewall commands or APIs)
        echo "IP Address " . htmlspecialchars($ip) . " has been unblocked.";
    } else {
        echo "Invalid IP address.";
    }
}
?>
