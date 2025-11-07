import socket

HOST = '127.0.0.1'
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"SOA Server listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        # Receive client's opening message
        data = conn.recv(1024).decode('utf-8')
        if data:
            print('Client:', data)
            if data.strip() == 'I am Client':
                reply = 'I am Server'
                conn.sendall(reply.encode('utf-8'))
                print('Server:', reply)
        # Continue a small dialogue
        data = conn.recv(1024).decode('utf-8')
        if data:
            print('Client:', data)
            if data.strip() == 'Nice to meet you!':
                reply = 'Nice to meet you too!'
                conn.sendall(reply.encode('utf-8'))
                print('Server:', reply)

    print('Connection closed')
