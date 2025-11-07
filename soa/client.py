"""
SOA Client - Service-Oriented Architecture Demo
================================================
This client demonstrates a simple Service-Oriented Architecture (SOA) pattern
by connecting to a remote service and exchanging messages.

Architecture:
- Transport Protocol: TCP/IP sockets
- Communication Style: Synchronous request-response
- Service Discovery: Direct connection (host:port hardcoded)

The client initiates a connection to the server and engages in a dialogue.
"""

import socket

# Server connection details
HOST = '127.0.0.1'  # Server IP address
PORT = 9000         # Server port number

print("=" * 60)
print("SOA CLIENT - Service-Oriented Architecture Demo")
print("=" * 60)
print(f"Connecting to SOA Server:")
print(f"  - Server: {HOST}:{PORT}")
print(f"  - Transport: TCP/IP Sockets")
print("=" * 60)

# Create a TCP/IP socket and connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"\n[CLIENT] Connecting to {HOST}:{PORT}...")
    s.connect((HOST, PORT))  # Establish connection
    print("[CLIENT] Connected successfully!")
    print("-" * 60)
    
    # === First Message Exchange ===
    # Send opening message to the server
    msg = 'I am Client'
    print(f'\n[SENDING] Client: {msg}')
    s.sendall(msg.encode('utf-8'))  # Encode string to bytes and send
    
    # Wait for server's response
    print("[RECEIVING] Waiting for server response...")
    data = s.recv(1024).decode('utf-8')  # Receive and decode response
    print(f'[RECEIVED] Server: {data}')
    
    # === Second Message Exchange ===
    # Continue the dialogue with a greeting
    msg2 = 'Nice to meet you!'
    print(f'\n[SENDING] Client: {msg2}')
    s.sendall(msg2.encode('utf-8'))
    
    # Wait for server's response
    print("[RECEIVING] Waiting for server response...")
    data = s.recv(1024).decode('utf-8')
    print(f'[RECEIVED] Server: {data}')
    
    print("\n" + "-" * 60)
    print("[CLIENT] Dialogue complete. Closing connection...")
    print("=" * 60)
