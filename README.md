Assignment: SOA, RPC/RMI, REST (Python)

Folders:
- soa: simple socket-based client/server dialogue
- rpc: simple XML-RPC server exposing greet(name) and a client
- rest: Flask Book Management API with a small test script

Requirements:
- Install dependencies: pip install -r requirements.txt
  Or: pip install Flask requests

Quick run (PowerShell):
# 1) SOA demo (combined server+client in one process)
python .\soa\demo.py

# 2) RPC demo (combined server+client in one process)
python .\rpc\demo.py

# 3) REST demo (combined server+client in one process)
python .\rest\demo.py

Alternative: run server and client separately:
# SOA: Terminal 1: python .\soa\server.py  |  Terminal 2: python .\soa\client.py
# RPC: Terminal 1: python .\rpc\server.py  |  Terminal 2: python .\rpc\client.py
# REST: Terminal 1: python .\rest\app.py   |  Terminal 2: python .\rest\test_rest.py

See 'report.md' for architecture explanations and comparisons.
