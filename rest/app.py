"""
REST API - Book Management System
==================================
This is a RESTful API server for managing a collection of books.

What is REST?
-------------
REST (Representational State Transfer) is an architectural style for building
web services that use HTTP methods to perform operations on resources.

REST Principles:
1. Resource-based: Everything is a resource (e.g., books)
2. HTTP Methods: GET (read), POST (create), PUT (update), DELETE (delete)
3. Stateless: Each request contains all information needed
4. Uniform Interface: Standardized way to interact with resources

Resource: Book
--------------
Each book has the following attributes:
- id (integer): Unique identifier
- title (string): Book title
- author (string): Author name
- price (float): Book price

API Endpoints:
--------------
GET    /books          - Retrieve all books
GET    /books/<id>     - Retrieve a specific book by ID
POST   /books          - Create a new book
PUT    /books/<id>     - Update an existing book
DELETE /books/<id>     - Delete a book

Usage:
------
1. Start the server: python app.py
2. Test with browser: http://127.0.0.1:5000/books
3. Test with Postman or curl for POST/PUT/DELETE operations
"""

from flask import Flask, jsonify, request, abort

# Create Flask application
app = Flask(__name__)

# In-memory database: dictionary mapping book ID to book data
# In a production system, this would be replaced with a real database
books = {
    1: {"title": "Distributed Systems", "author": "Tanenbaum", "price": 50.0},
    2: {"title": "Clean Code", "author": "Robert C. Martin", "price": 45.0}
}

# Counter for generating new book IDs
next_id = 3


@app.route('/books', methods=['GET'])
def get_books():
    """
    GET /books - Retrieve all books
    
    Returns:
        JSON object with all books (key: book ID, value: book data)
        
    Example Response:
        {
            "1": {"title": "...", "author": "...", "price": 50.0},
            "2": {"title": "...", "author": "...", "price": 45.0}
        }
    """
    # Convert integer keys to strings for JSON serialization
    return jsonify({str(k): v for k, v in books.items()})


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """
    GET /books/<id> - Retrieve a specific book
    
    Args:
        book_id (int): The ID of the book to retrieve
        
    Returns:
        JSON object with the book data
        
    Errors:
        404 Not Found - If book doesn't exist
    """
    b = books.get(book_id)
    if not b:
        abort(404)  # Return 404 Not Found if book doesn't exist
    return jsonify({str(book_id): b})


@app.route('/books', methods=['POST'])
def add_book():
    """
    POST /books - Create a new book
    
    Request Body (JSON):
        {
            "title": "Book Title",
            "author": "Author Name",
            "price": 29.99
        }
        
    Returns:
        JSON object with success message and new book ID
        HTTP Status: 201 Created
        
    Errors:
        400 Bad Request - If required fields are missing
    """
    global next_id
    
    # Get JSON data from request body
    data = request.get_json()
    
    # Validate that all required fields are present
    if not data or not all(k in data for k in ('title', 'author', 'price')):
        abort(400)  # Return 400 Bad Request if validation fails
    
    # Create new book entry
    books[next_id] = {
        "title": data['title'],
        "author": data['author'],
        "price": float(data['price'])
    }
    
    # Prepare response
    resp = {"message": "Book added", "id": next_id}
    next_id += 1
    
    return jsonify(resp), 201  # Return 201 Created status


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """
    PUT /books/<id> - Update an existing book
    
    Args:
        book_id (int): The ID of the book to update
        
    Request Body (JSON) - any combination of:
        {
            "title": "New Title",
            "author": "New Author",
            "price": 39.99
        }
        
    Returns:
        JSON object with success message and book ID
        
    Errors:
        404 Not Found - If book doesn't exist
        400 Bad Request - If request body is empty
    """
    data = request.get_json()
    
    # Check if book exists
    if book_id not in books:
        abort(404)
    
    # Validate request body
    if not data:
        abort(400)
    
    # Update only the fields that are provided
    books[book_id].update({k: data[k] for k in ('title', 'author', 'price') if k in data})
    
    return jsonify({"message": "Book updated", "id": book_id})


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """
    DELETE /books/<id> - Delete a book
    
    Args:
        book_id (int): The ID of the book to delete
        
    Returns:
        JSON object with success message and deleted book ID
        
    Errors:
        404 Not Found - If book doesn't exist
    """
    if book_id not in books:
        abort(404)
    
    # Remove book from dictionary
    del books[book_id]
    
    return jsonify({"message": "Book deleted", "id": book_id})


if __name__ == '__main__':
    print("=" * 70)
    print("REST API SERVER - Book Management System")
    print("=" * 70)
    print("API Endpoints:")
    print("  GET    /books       - Retrieve all books")
    print("  GET    /books/<id>  - Retrieve a specific book")
    print("  POST   /books       - Create a new book")
    print("  PUT    /books/<id>  - Update a book")
    print("  DELETE /books/<id>  - Delete a book")
    print("=" * 70)
    print("Server starting on http://127.0.0.1:5000")
    print("Press Ctrl+C to stop the server")
    print("=" * 70)
    
    app.run(host='127.0.0.1', port=5000)
