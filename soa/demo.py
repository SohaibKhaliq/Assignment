import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 9000


def server_thread():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"SOA Server listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024).decode('utf-8')
            if data:
                print('Client:', data)
                if data.strip() == 'I am Client':
                    reply = 'I am Server'
                    conn.sendall(reply.encode('utf-8'))
                    print('Server:', reply)
            data = conn.recv(1024).decode('utf-8')
            if data:
                print('Client:', data)
                if data.strip() == 'Nice to meet you!':
                    reply = 'Nice to meet you too!'
                    conn.sendall(reply.encode('utf-8'))
                    print('Server:', reply)
        print('Server: connection closed')


def client_run():
    time.sleep(0.5)  # wait for server to be ready
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = 'I am Client'
        print('Client:', msg)
        s.sendall(msg.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print('Server:', data)
        msg2 = 'Nice to meet you!'
        print('Client:', msg2)
        s.sendall(msg2.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print('Server:', data)


if __name__ == '__main__':
    t = threading.Thread(target=server_thread, daemon=True)
    t.start()
    client_run()
    time.sleep(0.2)
