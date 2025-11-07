"""
SOA Interactive Client - Service-Oriented Architecture Demo
===========================================================
This interactive client allows users to send custom messages to the server
and engage in a real-time dialogue.

Features:
- User can input custom messages
- Real-time communication with SOA server
- Graceful error handling

Usage:
1. Start the server: python server.py
2. Start this client: python client_interactive.py
3. Enter messages when prompted
"""

import socket
import sys

# Server connection details
HOST = '127.0.0.1'
PORT = 9000

print("=" * 60)
print("SOA INTERACTIVE CLIENT")
print("=" * 60)
print("This client allows you to send custom messages to the server.")
print(f"Server: {HOST}:{PORT}")
print("=" * 60)

try:
    # Create socket and connect
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"\n[CLIENT] Connecting to {HOST}:{PORT}...")
        s.connect((HOST, PORT))
        print("[CLIENT] ✓ Connected successfully!")
        print("\nYou can now send messages to the server.")
        print("Type your message and press Enter (or 'quit' to exit)")
        print("-" * 60)
        
        message_count = 0
        
        while True:
            # Get user input
            user_msg = input(f"\n[Message #{message_count + 1}] You: ").strip()
            
            # Check for exit command
            if user_msg.lower() in ['quit', 'exit', 'q']:
                print("\n[CLIENT] User requested exit. Closing connection...")
                break
            
            # Skip empty messages
            if not user_msg:
                print("[WARNING] Empty message. Please enter something.")
                continue
            
            # Send message to server
            print(f"[SENDING] → '{user_msg}'")
            s.sendall(user_msg.encode('utf-8'))
            message_count += 1
            
            # Receive response from server
            try:
                print("[RECEIVING] Waiting for server response...")
                s.settimeout(5.0)  # 5 second timeout
                data = s.recv(1024).decode('utf-8')
                
                if data:
                    print(f"[RECEIVED] ← Server: '{data}'")
                else:
                    print("[INFO] Server closed the connection.")
                    break
                    
            except socket.timeout:
                print("[TIMEOUT] No response from server within 5 seconds.")
                break
            except Exception as e:
                print(f"[ERROR] Failed to receive: {e}")
                break
        
        print("\n" + "=" * 60)
        print(f"[SUMMARY] Total messages sent: {message_count}")
        print("[CLIENT] Connection closed.")
        print("=" * 60)

except ConnectionRefusedError:
    print("\n[ERROR] ✗ Connection refused!")
    print("Make sure the server is running: python server.py")
    sys.exit(1)
except KeyboardInterrupt:
    print("\n\n[INFO] Interrupted by user (Ctrl+C)")
    sys.exit(0)
except Exception as e:
    print(f"\n[ERROR] An unexpected error occurred: {e}")
    sys.exit(1)
