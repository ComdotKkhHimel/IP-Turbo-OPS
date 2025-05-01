<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $ip = htmlspecialchars($_POST['ip']);
    $logFile = 'unblock_requests.log';

    file_put_contents($logFile, date('Y-m-d H:i:s') . " - IP requested unblock: $ip\n", FILE_APPEND);

    echo "Unblock request for IP $ip has been logged. Admin will review.";
} else {
    echo "Invalid request.";
}
?>
