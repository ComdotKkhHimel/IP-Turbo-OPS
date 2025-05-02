function unblockIP() {
  const ip = document.getElementById('ipInput').value.trim();
  const message = document.getElementById('message');
  const ipRegex = /^(\d{1,3}\.){3}\d{1,3}$/;

  if (ipRegex.test(ip)) {
    message.textContent = `IP Address ${ip} has been unblocked.`;
    message.style.color = 'green';
  } else {
    message.textContent = 'Invalid IP address. Please enter a valid IP.';
    message.style.color = 'red';
  }
}
