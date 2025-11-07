"""
RPC Interactive Server - Remote Procedure Call Demo (XML-RPC)
=============================================================
This interactive server exposes multiple remote methods that clients can call.

Available Remote Methods:
- greet(name: str) -> str
- add(a: int, b: int) -> int
- multiply(a: int, b: int) -> int
- get_server_info() -> dict
- echo(message: str) -> str

Features:
- Multiple remote methods exposed
- Request logging with timestamps
- Graceful shutdown handling

Usage:
1. Start this server: python server_interactive.py
2. Start the interactive client: python client_interactive.py
"""

from xmlrpc.server import SimpleXMLRPCServer
import datetime

# Server configuration
HOST = '127.0.0.1'
PORT = 9001

# Request counter for logging
request_counter = 0


def greet(name):
    """
    Remote method: Generate a personalized greeting.
    
    Args:
        name (str): Name of the person to greet
        
    Returns:
        str: Personalized greeting message
    """
    global request_counter
    request_counter += 1
    log_request('greet', f"name='{name}'")
    return f"Hello {name}, this is the server!"


def add(a, b):
    """
    Remote method: Add two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Sum of a and b
    """
    global request_counter
    request_counter += 1
    log_request('add', f"a={a}, b={b}")
    result = a + b
    print(f"    → Result: {result}")
    return result


def multiply(a, b):
    """
    Remote method: Multiply two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Product of a and b
    """
    global request_counter
    request_counter += 1
    log_request('multiply', f"a={a}, b={b}")
    result = a * b
    print(f"    → Result: {result}")
    return result


def get_server_info():
    """
    Remote method: Get server information.
    
    Returns:
        dict: Dictionary containing server details
    """
    global request_counter
    request_counter += 1
    log_request('get_server_info', 'no parameters')
    
    info = {
        'server_type': 'XML-RPC',
        'host': HOST,
        'port': PORT,
        'total_requests': request_counter,
        'timestamp': str(datetime.datetime.now())
    }
    return info


def echo(message):
    """
    Remote method: Echo back the received message.
    
    Args:
        message (str): Message to echo
        
    Returns:
        str: The same message with prefix
    """
    global request_counter
    request_counter += 1
    log_request('echo', f"message='{message}'")
    return f"Server echoes: {message}"


def log_request(method_name, params):
    """Log an incoming RPC request."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{timestamp}] RPC Call #{request_counter}")
    print(f"  Method: {method_name}({params})")


print("=" * 70)
print("RPC INTERACTIVE SERVER - Remote Procedure Call Demo (XML-RPC)")
print("=" * 70)
print(f"Configuration:")
print(f"  - Host: {HOST}")
print(f"  - Port: {PORT}")
print(f"  - Protocol: XML-RPC")
print("\nExposed Remote Methods:")
print("  1. greet(name: str) -> str")
print("  2. add(a: int, b: int) -> int")
print("  3. multiply(a: int, b: int) -> int")
print("  4. get_server_info() -> dict")
print("  5. echo(message: str) -> str")
print("=" * 70)

# Create XML-RPC server
server = SimpleXMLRPCServer((HOST, PORT), allow_none=True)

# Register all remote methods
server.register_function(greet, 'greet')
server.register_function(add, 'add')
server.register_function(multiply, 'multiply')
server.register_function(get_server_info, 'get_server_info')
server.register_function(echo, 'echo')

print(f"\n[SERVER] ✓ XML-RPC Server listening on {HOST}:{PORT}")
print("[SERVER] All methods registered and ready!")
print("[INFO] Press Ctrl+C to stop the server")
print("-" * 70)

try:
    server.serve_forever()
except KeyboardInterrupt:
    print(f'\n\n[SERVER] Received shutdown signal')
    print(f"[SUMMARY] Total RPC calls processed: {request_counter}")
    print('[SERVER] Shutting down...')
    print("=" * 70)
