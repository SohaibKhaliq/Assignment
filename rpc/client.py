"""
RPC Client - Remote Procedure Call Demo (XML-RPC)
==================================================
This client demonstrates how to call remote methods on a server using RPC.

Key Concepts:
- The client creates a proxy object that represents the remote server
- Method calls on the proxy are automatically serialized and sent to the server
- The server executes the method and returns the result
- The result is deserialized and returned to the client

From the client's perspective, calling a remote method looks just like
calling a local function!

Usage:
1. Start the RPC server: python server.py
2. Run this client: python client.py
"""

import xmlrpc.client

# Server endpoint URL
HOST = 'http://127.0.0.1:9001'

print("=" * 60)
print("RPC CLIENT - Remote Procedure Call Demo (XML-RPC)")
print("=" * 60)
print(f"Connecting to RPC Server: {HOST}")
print("=" * 60)

# Create a proxy object to the remote server
# All method calls on 'proxy' will be sent to the server
print(f"\n[CLIENT] Creating proxy connection to {HOST}...")
proxy = xmlrpc.client.ServerProxy(HOST)
print("[CLIENT] ✓ Proxy created successfully!")

# Call the remote method 'greet' with parameter 'Ali'
print("\n[RPC CALL] Invoking remote method: greet('Ali')")
print("[CLIENT] Requesting remote method...")
print("-" * 60)

# This looks like a local function call, but it's actually happening on the server!
response = proxy.greet('Ali')

print(f"[RESPONSE] Response from Server: {response}")
print("-" * 60)

print("\n[SUCCESS] Remote procedure call completed successfully!")
print("=" * 60)

# Technical Details
print("\nWhat just happened?")
print("1. Client serialized the method call 'greet(\"Ali\")' to XML")
print("2. Client sent XML data over HTTP to the server")
print("3. Server deserialized the XML and executed greet('Ali')")
print("4. Server serialized the result to XML")
print("5. Client received and deserialized the XML response")
print("=" * 60)
