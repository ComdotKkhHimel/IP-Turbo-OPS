from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import subprocess

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/unblock', methods=['POST'])
def unblock_ip():
    data = request.get_json()
    ip = data.get('ip')
    if not ip:
        return jsonify({'error': 'IP address is required'}), 400
    try:
        subprocess.run(['iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'], check=True)
        return jsonify({'status': f'IP {ip} unblocked successfully'})
    except subprocess.CalledProcessError:
        return jsonify({'error': f'Could not unblock {ip}. It may not be blocked.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
