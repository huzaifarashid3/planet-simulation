from flask import Flask, render_template, request
import socket

app = Flask(__name__)

# Function to send data to a socket
def send_to_socket(value):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 5001))  # Adjust the address and port as needed
        s.sendall(str(value).encode())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/slider', methods=['POST'])
def slider():
    value = request.json.get('value')
    send_to_socket(value)
    return {'status': 'success', 'value': value}

if __name__ == '__main__':
    app.run(debug=True)
