from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory books store: id -> dict
books = {
    1: {"title": "Distributed Systems", "author": "Tanenbaum", "price": 50.0},
    2: {"title": "Clean Code", "author": "Robert C. Martin", "price": 45.0}
}
next_id = 3

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({str(k): v for k, v in books.items()})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    b = books.get(book_id)
    if not b:
        abort(404)
    return jsonify({str(book_id): b})

@app.route('/books', methods=['POST'])
def add_book():
    global next_id
    data = request.get_json()
    if not data or not all(k in data for k in ('title', 'author', 'price')):
        abort(400)
    books[next_id] = {"title": data['title'], "author": data['author'], "price": float(data['price'])}
    resp = {"message": "Book added", "id": next_id}
    next_id += 1
    return jsonify(resp), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    if book_id not in books:
        abort(404)
    if not data:
        abort(400)
    books[book_id].update({k: data[k] for k in ('title','author','price') if k in data})
    return jsonify({"message": "Book updated", "id": book_id})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id not in books:
        abort(404)
    del books[book_id]
    return jsonify({"message": "Book deleted", "id": book_id})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
