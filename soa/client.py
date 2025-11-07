import socket

HOST = '127.0.0.1'
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = 'I am Client'
    print('Client:', msg)
    s.sendall(msg.encode('utf-8'))

    data = s.recv(1024).decode('utf-8')
    print('Server:', data)

    # Continue dialogue
    msg2 = 'Nice to meet you!'
    print('Client:', msg2)
    s.sendall(msg2.encode('utf-8'))

    data = s.recv(1024).decode('utf-8')
    print('Server:', data)
