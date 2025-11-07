"""
RPC Server - Remote Procedure Call Demo (XML-RPC)
==================================================
This server demonstrates Remote Procedure Call (RPC) architecture using Python's
built-in XML-RPC library.

What is RPC?
------------
Remote Procedure Call (RPC) allows a client to execute functions on a remote server
as if they were local function calls. The RPC framework handles:
- Serialization of arguments
- Network communication
- Deserialization of results
- Error propagation

Architecture:
- Protocol: XML-RPC (HTTP-based, XML-encoded)
- Communication Style: Synchronous function calls
- Coupling: Tighter than SOA - clients must know function signatures

Available Remote Methods:
- greet(name: str) -> str: Returns a personalized greeting
"""

from xmlrpc.server import SimpleXMLRPCServer

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 9001         # XML-RPC service port

def greet(name):
    """
    Remote method: Generate a personalized greeting.
    
    This function is exposed as a remote method that clients can call over the network.
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: A personalized greeting message
        
    Example:
        Client calls: greet("Ali")
        Server returns: "Hello Ali, this is the server!"
    """
    return f"Hello {name}, this is the server!"


print("=" * 60)
print("RPC SERVER - Remote Procedure Call Demo (XML-RPC)")
print("=" * 60)
print(f"Configuration:")
print(f"  - Host: {HOST}")
print(f"  - Port: {PORT}")
print(f"  - Protocol: XML-RPC (HTTP + XML)")
print(f"  - Communication: Synchronous RPC")
print("\nExposed Remote Methods:")
print(f"  - greet(name: str) -> str")
print("=" * 60)

# Create XML-RPC server
server = SimpleXMLRPCServer((HOST, PORT), allow_none=True)

# Register the remote method
server.register_function(greet, 'greet')

print(f"\n[SERVER] ✓ XML-RPC Server listening on {HOST}:{PORT}")
print("[SERVER] Waiting for remote procedure calls...")
print("[INFO] Press Ctrl+C to stop the server")
print("-" * 60)

try:
    # Start serving requests (infinite loop)
    server.serve_forever()
except KeyboardInterrupt:
    print('\n\n[SERVER] Shutting down XML-RPC server...')
    print("=" * 60)
