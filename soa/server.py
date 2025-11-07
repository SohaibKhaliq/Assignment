"""
SOA Server - Service-Oriented Architecture Demo
================================================
This server demonstrates a simple Service-Oriented Architecture (SOA) pattern
using TCP sockets for message-based communication between distributed services.

Architecture:
- Transport Protocol: TCP/IP sockets
- Communication Style: Synchronous, message-oriented
- Coupling: Loosely coupled - services communicate via messages

The server listens for incoming connections and exchanges messages with clients.
"""

import socket

# Server configuration
HOST = '127.0.0.1'  # Localhost - server binds to this IP address
PORT = 9000         # Port number for the service endpoint

print("=" * 60)
print("SOA SERVER - Service-Oriented Architecture Demo")
print("=" * 60)
print(f"Configuration:")
print(f"  - Host: {HOST}")
print(f"  - Port: {PORT}")
print(f"  - Transport: TCP/IP Sockets")
print(f"  - Communication: Message-based, Synchronous")
print("=" * 60)

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port
    s.bind((HOST, PORT))
    
    # Listen for incoming connections (max 1 queued connection)
    s.listen(1)
    print(f"\n[SERVER] Listening on {HOST}:{PORT}")
    print("[SERVER] Waiting for client connection...")
    
    # Accept a connection (blocks until a client connects)
    conn, addr = s.accept()
    
    with conn:
        print(f"\n[CONNECTION] Client connected from {addr}")
        print("-" * 60)
        
        # === First Message Exchange ===
        # Receive the client's opening message
        print("\n[RECEIVING] Waiting for client message...")
        data = conn.recv(1024).decode('utf-8')  # Buffer size: 1024 bytes
        
        if data:
            print(f'[CLIENT]: {data}')
            
            # Check if it's the expected opening message
            if data.strip() == 'I am Client':
                reply = 'I am Server'
                conn.sendall(reply.encode('utf-8'))  # Send response
                print(f'[SERVER]: {reply}')
        
        # === Second Message Exchange ===
        # Continue the dialogue
        print("\n[RECEIVING] Waiting for next client message...")
        data = conn.recv(1024).decode('utf-8')
        
        if data:
            print(f'[CLIENT]: {data}')
            
            # Respond to greeting
            if data.strip() == 'Nice to meet you!':
                reply = 'Nice to meet you too!'
                conn.sendall(reply.encode('utf-8'))
                print(f'[SERVER]: {reply}')

    print("\n" + "-" * 60)
    print('[CONNECTION] Client disconnected')
    print('[SERVER] Shutting down...')
    print("=" * 60)
