from flask import Flask, jsonify, request
app = Flask(__name__)
books = [
    {"id": 1, "title": "1984","author": "George Orwell"},
    {"id": 2, "title": "To kill a Mockingbird","author":"Harper Lee"}
]

@app.route('/books', methods=['GET'])
def get_books(): 
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def add_book(): 
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book),201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_data = request.get_json()
    for book in books: 
        if book["id"] == book_id:
            book.update(updated_data)
            return jsonify(book),404
        
        
@app.route('/books/<int:book_id>',methods=['DELETE'])
def delete_books(book_id): 
    global books
    books = [b for b in books if b['id'] != book_id]
    return ("Book deleted", 204)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 - Page Not Found</h1><p>Check your URL and try again.</p>", 404


if __name__ == '__main__': 
    app.run(debug=True)