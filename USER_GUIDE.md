# User Guide - Distributed Systems Assignment

## Overview

This assignment demonstrates three distributed system architectures:
1. **SOA** (Service-Oriented Architecture) - Message-based communication
2. **RPC** (Remote Procedure Call) - Remote method invocation
3. **REST** (Representational State Transfer) - Resource-based HTTP API

Each architecture has been implemented with:
- ✅ Comprehensive documentation and comments
- ✅ Interactive user interfaces
- ✅ Automated demo scripts
- ✅ Error handling and validation

---

## Getting Started

### Prerequisites
```powershell
# Install required Python packages
pip install Flask requests
```

### Project Structure
```
Assignment/
├── soa/                    # Service-Oriented Architecture
│   ├── server.py          # Basic server (documented)
│   ├── client.py          # Basic client (documented)
│   ├── server_interactive.py  # Interactive server
│   ├── client_interactive.py  # Interactive client
│   └── demo.py            # All-in-one demo
├── rpc/                    # Remote Procedure Call
│   ├── server.py          # Basic RPC server (documented)
│   ├── client.py          # Basic RPC client (documented)
│   ├── server_interactive.py  # Multi-method server
│   ├── client_interactive.py  # Interactive menu client
│   └── demo.py            # All-in-one demo
├── rest/                   # RESTful API
│   ├── app.py             # Flask API server (documented)
│   ├── test_rest.py       # Automated API tests
│   ├── client_interactive.py  # Interactive CRUD client
│   └── demo.py            # All-in-one demo
├── README.md              # Quick reference
├── report.md              # Architecture analysis
└── USER_GUIDE.md          # This file
```

---

## Quick Start (Automated Demos)

These demos are perfect for assignment submission demonstrations:

### 1. SOA Demo
```powershell
python .\soa\demo.py
```
**Expected Output:**
```
Client: I am Client
Server: I am Server
Client: Nice to meet you!
Server: Nice to meet you too!
```

### 2. RPC Demo
```powershell
python .\rpc\demo.py
```
**Expected Output:**
```
Requesting remote method...
Response from Server: Hello Ali, this is the server!
```

### 3. REST Demo
```powershell
python .\rest\demo.py
```
**Expected Output:**
```
GET /books
200 {'1': {...}, '2': {...}}

POST /books
201 {'id': 3, 'message': 'Book added'}
...
```

---

## Interactive Mode (Recommended for Learning)

### SOA Interactive

**Step 1:** Start the server
```powershell
python .\soa\server_interactive.py
```

**Step 2:** In a new terminal, start the client
```powershell
python .\soa\client_interactive.py
```

**What You Can Do:**
- Type custom messages and send them to the server
- Server responds intelligently based on message content
- Try messages like: "Hello", "How are you?", "Help"
- Type 'quit' to exit

**Example Session:**
```
[Message #1] You: Hello there!
[RESPONSE] Server: Hello! Nice to hear from you.

[Message #2] You: How are you?
[RESPONSE] Server: I am functioning optimally. Thank you for asking!
```

---

### RPC Interactive

**Step 1:** Start the server
```powershell
python .\rpc\server_interactive.py
```

**Step 2:** In a new terminal, start the client
```powershell
python .\rpc\client_interactive.py
```

**Available Remote Methods:**
1. **greet(name)** - Get a personalized greeting
2. **add(a, b)** - Add two numbers on the server
3. **multiply(a, b)** - Multiply two numbers on the server
4. **get_server_info()** - Get server statistics and info
5. **echo(message)** - Echo a message back

**Example Session:**
```
Choose a remote method to call:
  1. greet(name)
  2. add(a, b)
  ...

Enter your choice: 1
Enter a name to greet: John
[RESPONSE] Hello John, this is the server!
```

---

### REST Interactive

**Step 1:** Start the API server
```powershell
python .\rest\app.py
```

**Step 2:** In a new terminal, start the interactive client
```powershell
python .\rest\client_interactive.py
```

**Available Operations:**
1. **View all books** - GET /books
2. **View specific book** - GET /books/<id>
3. **Add new book** - POST /books
4. **Update book** - PUT /books/<id>
5. **Delete book** - DELETE /books/<id>

**Example Session:**
```
BOOK MANAGEMENT MENU
  1. View all books
  2. View a specific book
  3. Add a new book
  ...

Enter your choice: 3

ADD NEW BOOK
Enter book title: Python Programming
Enter author name: John Doe
Enter price: 29.99
[SUCCESS] Book added successfully! (ID: 3)
```

---

## Documentation Features

### All Source Files Include:

1. **Module Docstrings** - Explain what each file does
2. **Function Docstrings** - Describe parameters, returns, and examples
3. **Inline Comments** - Explain complex logic
4. **Architecture Explanations** - What, why, and how
5. **Error Handling** - Graceful failure with helpful messages

### Example Documentation (from rpc/server.py):
```python
"""
RPC Server - Remote Procedure Call Demo (XML-RPC)
==================================================
This server demonstrates Remote Procedure Call (RPC) architecture...

What is RPC?
------------
Remote Procedure Call (RPC) allows a client to execute functions...
"""

def greet(name):
    """
    Remote method: Generate a personalized greeting.
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: A personalized greeting message
    """
```

---

## Testing the APIs

### Manual Testing with Browser
For REST API, you can use your web browser:
```
http://127.0.0.1:5000/books
```

### Testing with PowerShell (curl alternative)
```powershell
# GET all books
Invoke-RestMethod -Uri "http://127.0.0.1:5000/books" -Method GET

# POST new book
$body = @{
    title = "Test Book"
    author = "Test Author"
    price = 19.99
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:5000/books" -Method POST -Body $body -ContentType "application/json"
```

### Testing with Postman
1. Download Postman (https://www.postman.com/)
2. Import the following requests:
   - GET http://127.0.0.1:5000/books
   - POST http://127.0.0.1:5000/books (with JSON body)
   - PUT http://127.0.0.1:5000/books/1 (with JSON body)
   - DELETE http://127.0.0.1:5000/books/1

---

## Troubleshooting

### "Connection Refused" Error
**Problem:** Client cannot connect to server
**Solution:** Make sure the server is running first
```powershell
# Start server in Terminal 1
python .\soa\server.py

# Then start client in Terminal 2
python .\soa\client.py
```

### "Port Already in Use" Error
**Problem:** Port is occupied by another process
**Solution:** 
1. Close the previous server instance
2. Or change the PORT variable in both server and client files

### "Module Not Found: Flask"
**Problem:** Flask is not installed
**Solution:**
```powershell
pip install Flask requests
```

### Interactive Client Shows No Response
**Problem:** Server might have stopped
**Solution:** Check server terminal for errors, restart if needed

---

## Assignment Deliverables Checklist

✅ **Task 1 - SOA Implementation**
- [x] Client-Server communication using sockets
- [x] Two-way dialogue
- [x] Comprehensive documentation

✅ **Task 2 - RPC Implementation**
- [x] XML-RPC server with greet() method
- [x] Client calling remote method
- [x] Extended with multiple methods (interactive version)

✅ **Task 3 - REST Implementation**
- [x] Flask API with Book resource
- [x] Full CRUD operations (GET/POST/PUT/DELETE)
- [x] Interactive client for testing

✅ **Documentation**
- [x] Source code with docstrings and comments
- [x] report.md with architecture comparison
- [x] README.md with quick start
- [x] USER_GUIDE.md (this file)

✅ **Bonus Features**
- [x] Interactive user interfaces
- [x] Error handling and validation
- [x] Multiple demo modes
- [x] Professional formatting and logging

---

## Key Learning Points

### SOA (Service-Oriented Architecture)
- **Communication:** Message-based, TCP sockets
- **Coupling:** Loose - services only need to understand messages
- **Use Case:** Microservices, event-driven systems

### RPC (Remote Procedure Call)
- **Communication:** Function calls over network (XML-RPC)
- **Coupling:** Tighter - clients must know function signatures
- **Use Case:** Distributed computing, internal service calls

### REST (Representational State Transfer)
- **Communication:** HTTP methods on resources
- **Coupling:** Loose - uniform interface, stateless
- **Use Case:** Public APIs, web services, mobile backends

---

## Further Exploration

### Extend SOA
- Add JSON message format
- Implement async communication
- Add service discovery

### Extend RPC
- Switch to gRPC for better performance
- Add authentication
- Implement streaming RPC

### Extend REST
- Add database persistence (SQLite/PostgreSQL)
- Implement authentication (JWT tokens)
- Add pagination and filtering
- Create OpenAPI/Swagger documentation

---

## Support

For questions or issues:
1. Review the comprehensive comments in source files
2. Check report.md for architecture explanations
3. Run demo scripts to see expected output
4. Use interactive clients for hands-on learning

**Happy Learning! 🚀**
