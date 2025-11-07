from xmlrpc.server import SimpleXMLRPCServer
import threading
import time
import xmlrpc.client

HOST = '127.0.0.1'
PORT = 9001


def greet(name):
    return f"Hello {name}, this is the server!"


def server_thread():
    server = SimpleXMLRPCServer((HOST, PORT), allow_none=True, logRequests=False)
    server.register_function(greet, 'greet')
    print(f"XML-RPC Server listening on {HOST}:{PORT}")
    server.serve_forever()


if __name__ == '__main__':
    t = threading.Thread(target=server_thread, daemon=True)
    t.start()
    time.sleep(0.3)
    proxy = xmlrpc.client.ServerProxy(f'http://{HOST}:{PORT}')
    print('Requesting remote method...')
    resp = proxy.greet('Ali')
    print('Response from Server:', resp)
    # give server thread a moment
    time.sleep(0.2)
