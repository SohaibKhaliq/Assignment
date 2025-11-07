from xmlrpc.server import SimpleXMLRPCServer

HOST = '127.0.0.1'
PORT = 9001

def greet(name):
    return f"Hello {name}, this is the server!"

server = SimpleXMLRPCServer((HOST, PORT), allow_none=True)
server.register_function(greet, 'greet')
print(f"XML-RPC Server listening on {HOST}:{PORT}")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print('Shutting down XML-RPC server')
