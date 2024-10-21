import socket

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('58.65.198.92', 5001))
        s.listen()
        print("Socket server is listening on port 5001...")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                return int(data.decode())
                print('Received', data.decode())

if __name__ == '__main__':
    start_server()
