import xmlrpc.client

HOST = 'http://127.0.0.1:9001'
proxy = xmlrpc.client.ServerProxy(HOST)

print('Requesting remote method...')
resp = proxy.greet('Ali')
print('Response from Server:', resp)
