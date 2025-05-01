from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/unblock', methods=['POST'])
def unblock_ip():
    data = request.get_json()
    ip = data.get('ip')
    if not ip:
        return jsonify({'error': 'Missing IP'}), 400
    try:
        subprocess.run(['iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'], check=True)
        return jsonify({'status': f'IP {ip} unblocked'})
    except subprocess.CalledProcessError:
        return jsonify({'error': 'Failed to unblock IP'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
