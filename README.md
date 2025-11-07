Assignment: SOA, RPC/RMI, REST (Python)

This project demonstrates three distributed system architectures with comprehensive
documentation and interactive user interfaces.

Folders:
--------
- soa/  : Service-Oriented Architecture (Socket-based messaging)
- rpc/  : Remote Procedure Call (XML-RPC)
- rest/ : RESTful API (Flask Book Management System)

Requirements:
-------------
Install dependencies:
  pip install -r requirements.txt
Or:
  pip install Flask requests

================================================================================
QUICK RUN - Demo Scripts (Automated)
================================================================================

These demos run server and client in a single process for easy testing:

1) SOA Demo (Service-Oriented Architecture)
   python .\soa\demo.py

2) RPC Demo (Remote Procedure Call)
   python .\rpc\demo.py

3) REST Demo (RESTful API)
   python .\rest\demo.py

================================================================================
INTERACTIVE MODE - User Input (Recommended)
================================================================================

For hands-on experience with user interaction:

1) SOA Interactive:
   Terminal 1: python .\soa\server_interactive.py
   Terminal 2: python .\soa\client_interactive.py
   
   Features:
   - Send custom messages to the server
   - Real-time two-way communication
   - Intelligent server responses

2) RPC Interactive:
   Terminal 1: python .\rpc\server_interactive.py
   Terminal 2: python .\rpc\client_interactive.py
   
   Available remote methods:
   - greet(name)         : Get personalized greeting
   - add(a, b)           : Add two numbers
   - multiply(a, b)      : Multiply two numbers
   - get_server_info()   : Get server information
   - echo(message)       : Echo a message

3) REST Interactive:
   Terminal 1: python .\rest\app.py
   Terminal 2: python .\rest\client_interactive.py
   
   Interactive menu for:
   - GET all books
   - GET specific book by ID
   - POST (create) new book
   - PUT (update) existing book
   - DELETE book

================================================================================
STANDARD MODE - Separate Server/Client
================================================================================

Run server and client in separate terminals:

SOA:
  Terminal 1: python .\soa\server.py
  Terminal 2: python .\soa\client.py

RPC:
  Terminal 1: python .\rpc\server.py
  Terminal 2: python .\rpc\client.py

REST:
  Terminal 1: python .\rest\app.py
  Terminal 2: python .\rest\test_rest.py

================================================================================
FILE DESCRIPTIONS
================================================================================

SOA (Service-Oriented Architecture):
  - server.py              : Basic TCP socket server with detailed logging
  - client.py              : Basic TCP socket client
  - server_interactive.py  : Interactive server with intelligent responses
  - client_interactive.py  : Interactive client for custom messages
  - demo.py               : Combined server+client demo

RPC (Remote Procedure Call):
  - server.py              : XML-RPC server exposing greet() method
  - client.py              : Basic RPC client calling greet()
  - server_interactive.py  : Interactive server with 5 remote methods
  - client_interactive.py  : Interactive client with method menu
  - demo.py               : Combined server+client demo

REST (RESTful Architecture):
  - app.py                 : Flask REST API with full CRUD operations
  - test_rest.py           : Automated test script for all endpoints
  - client_interactive.py  : Interactive menu-driven REST client
  - demo.py               : Combined server+client demo

Documentation:
  - report.md             : Architecture explanations and comparisons
  - README.md            : This file

================================================================================

See 'report.md' for:
- Detailed architecture explanations
- Communication style comparisons
- Scalability analysis
- Coupling differences
- When to use each architecture
