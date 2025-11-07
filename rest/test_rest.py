import requests

BASE = 'http://127.0.0.1:5000'

print('GET /books')
r = requests.get(f'{BASE}/books')
print(r.status_code, r.json())

print('\nPOST /books')
r = requests.post(f'{BASE}/books', json={"title": "New Book", "author": "Someone", "price": 12.5})
print(r.status_code, r.json())

print('\nGET /books/3')
r = requests.get(f'{BASE}/books/3')
print(r.status_code, r.json())

print('\nPUT /books/3')
r = requests.put(f'{BASE}/books/3', json={"price": 15.0})
print(r.status_code, r.json())

print('\nDELETE /books/3')
r = requests.delete(f'{BASE}/books/3')
print(r.status_code, r.json())

print('\nFinal GET /books')
r = requests.get(f'{BASE}/books')
print(r.status_code, r.json())
