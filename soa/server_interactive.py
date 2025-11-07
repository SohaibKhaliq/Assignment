"""
SOA Interactive Server - Service-Oriented Architecture Demo
===========================================================
This interactive server responds to any message from clients and allows
for multi-message exchanges.

Features:
- Handles multiple messages from a single client connection
- Echoes received messages or provides intelligent responses
- Comprehensive logging of all interactions

Usage:
1. Start this server: python server_interactive.py
2. In another terminal, start the client: python client_interactive.py
"""

import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 9000

print("=" * 60)
print("SOA INTERACTIVE SERVER")
print("=" * 60)
print(f"Configuration:")
print(f"  - Host: {HOST}")
print(f"  - Port: {PORT}")
print(f"  - Mode: Interactive Multi-Message")
print("=" * 60)

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Allow socket reuse
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind and listen
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"\n[SERVER] ✓ Listening on {HOST}:{PORT}")
    print("[SERVER] Waiting for client connection...")
    
    # Accept connection
    conn, addr = s.accept()
    
    with conn:
        print(f"\n[CONNECTION] ✓ Client connected from {addr}")
        print("-" * 60)
        print("Server is now ready to receive messages.")
        print("The server will respond to each message until the client disconnects.")
        print("-" * 60)
        
        message_count = 0
        
        # Continuous message loop
        while True:
            try:
                # Receive message from client
                print(f"\n[RECEIVING] Waiting for message #{message_count + 1}...")
                data = conn.recv(1024).decode('utf-8')
                
                # Check if client disconnected
                if not data:
                    print("[INFO] Client has closed the connection.")
                    break
                
                message_count += 1
                print(f'[CLIENT MESSAGE #{message_count}]: "{data}"')
                
                # Generate intelligent response based on message content
                response = generate_response(data, message_count)
                
                # Send response back to client
                conn.sendall(response.encode('utf-8'))
                print(f'[SERVER RESPONSE]: "{response}"')
                
            except ConnectionResetError:
                print("\n[ERROR] Connection was reset by client.")
                break
            except Exception as e:
                print(f"\n[ERROR] An error occurred: {e}")
                break
        
        print("\n" + "=" * 60)
        print(f"[SUMMARY] Total messages processed: {message_count}")
        print('[CONNECTION] Client disconnected')
        print('[SERVER] Shutting down...')
        print("=" * 60)


def generate_response(message, count):
    """
    Generate an intelligent response based on the received message.
    
    Args:
        message (str): The message received from client
        count (int): The message sequence number
        
    Returns:
        str: The response to send back
    """
    msg_lower = message.lower().strip()
    
    # Predefined responses for common messages
    if msg_lower == 'i am client':
        return 'I am Server'
    elif 'hello' in msg_lower or 'hi' in msg_lower:
        return 'Hello! Nice to hear from you.'
    elif 'nice to meet you' in msg_lower:
        return 'Nice to meet you too!'
    elif 'how are you' in msg_lower:
        return 'I am functioning optimally. Thank you for asking!'
    elif 'bye' in msg_lower or 'goodbye' in msg_lower:
        return 'Goodbye! Thanks for connecting.'
    elif 'help' in msg_lower:
        return 'I am a simple SOA server. I respond to your messages!'
    elif '?' in message:
        return f'That is an interesting question! (Message #{count})'
    else:
        # Default echo response with confirmation
        return f'Server received: "{message}" (Message #{count})'
