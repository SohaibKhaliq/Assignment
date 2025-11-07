Service-Oriented Architecture (SOA) — Assignment Report

Overview

This project demonstrates three architectural styles and communication methods:
1) SOA-like client/server message exchange using sockets (simple service messaging)
2) RPC (XML-RPC) where the client calls a remote method on the server
3) RESTful architecture implemented with Flask for a Book Management System

Task 1 — SOA (Client & Server Communication)

Implementation
- Language: Python
- Transport: TCP sockets (socket module)
- Files: `soa/server.py`, `soa/client.py`

Behavior
- The client connects to the server and sends the message "I am Client".
- The server replies "I am Server".
- The client sends "Nice to meet you!" and server replies "Nice to meet you too!".

Analysis
- Communication is message-oriented and synchronous over TCP.
- Services are independent programs (processes) and loosely coupled by the agreed message protocol.

Task 2 — RPC (Remote Procedure Call)

Implementation
- Language: Python
- Library: Python's built-in `xmlrpc.server` and `xmlrpc.client`
- Files: `rpc/server.py`, `rpc/client.py`

Behavior
- Server exposes `greet(name)` which returns a greeting string.
- Client calls `greet('Ali')` remotely and prints the server response.

Analysis
- RPC gives the appearance of calling a local function while executing remotely.
- RPC is more tightly coupled than plain message passing because it implies a function signature and semantics.

Task 3 — REST Architecture — Book Management System

Implementation
- Language: Python
- Framework: Flask
- Files: `rest/app.py`, `rest/test_rest.py`

API Endpoints
- GET /books → returns all books
- GET /books/<id> → returns a single book
- POST /books → create a new book
- PUT /books/<id> → update a book
- DELETE /books/<id> → delete a book

Notes
- Books are stored in-memory (dictionary). This is suitable for the assignment but not persistent.

Comparison: SOA (message), RPC, REST

Communication style
- SOA (here, socket messaging): message-based. Could be synchronous or asynchronous. Requires custom message formats.
- RPC: procedure-call style — client invokes functions on server and expects return values.
- REST: resource-oriented over HTTP with standardized verbs (GET/POST/PUT/DELETE).

Scalability
- SOA (sockets) can scale but needs more infrastructure for discovery, load balancing, and message routing.
- RPC can be scaled with additional middleware but often requires careful versioning to avoid breaking clients.
- REST scales well: HTTP caching, statelessness, proxies, CDNs, and heterogeneous clients make REST favorable.

Coupling
- Message-based SOA: low coupling if messages are self-describing (e.g., JSON), but protocol must be known.
- RPC: tighter coupling due to method signatures and semantics.
- REST: loose coupling — clients and servers exchange representations of resources; the interface is uniform (HTTP verbs).

When to use which
- Use message-based services for asynchronous, event-driven systems or when you need flexible message schemas.
- Use RPC for distributed systems where operations map naturally to remote method calls and tight integration is acceptable.
- Use REST for public HTTP APIs, web services, and when you want stateless, cacheable operations over HTTP.

How to run
- Install dependencies: `pip install -r requirements.txt`
- See `README.md` for the quick run steps. Each demo starts a server (background) and runs a client/test script.

Deliverables
- Source code: `soa/`, `rpc/`, `rest/`
- Report: this `report.md`

