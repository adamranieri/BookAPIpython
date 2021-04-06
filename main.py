from flask import Flask, jsonify, request, abort
from daos.book_dao_local import BookDaoLocal
from entities.book import Book
from exceptions.resource_not_found import ResourceNotFound
from services.book_service_impl import BookServiceImpl


app = Flask(__name__)

book_dao = BookDaoLocal()
book_service = BookServiceImpl(book_dao)


@app.route('/books', methods=['GET'])
def get_all_books():
    title = request.args.get('title')
    if title == None:
        books = book_service.retrieve_all_books()
        dict_list = [book.json() for book in books]
        return jsonify(dict_list)
    else:
        books = book_service.get_books_by_title(title)
        dict_list = [book.json() for book in books]
        return jsonify(dict_list)


@app.route('/books', methods=['POST'])
def post_book():
    book = Book.json_deserialize(request.json)
    book_service.register_book(book)
    return jsonify(book.json()), 201


@app.route('/books/<book_id>', methods=['GET'])
def get_book(book_id: str):
    try:
        book = book_service.retrieve_book_by_id(int(book_id))
        return jsonify(book.json())
    except ResourceNotFound as e:
        return e.message,404


@app.route('/books/<book_id>', methods=['PUT'])
def put_book(book_id: str):
    try:
        book = Book.json_deserialize(request.json)
        book.book_id = int(book_id)
        book_service.update_book(book)
        return jsonify(book.json())
    except ResourceNotFound as e:
        return e.message, 404


@app.route('/books/<book_id>', methods=['DELETE'])
def del_book(book_id: str):
    try:
        book_service.delete_book_by_id(int(book_id))
        return '',204
    except ResourceNotFound as e:
        return e.message, 404

@app.route('/books/<book_id>', methods=['PATCH'])
def patch_book(book_id: str):
    action = request.json['action']

    if action == 'checkout':
        book_service.checkout_book(int(book_id))
        return 'The book was successfully checked out'
    elif action == 'checkin':
        book_service.checkin_book(int(book_id))
        return 'The book was successfully checked in'
    else:
        abort(400,'body must have a json with an action property and values checkin or checkout')




if __name__ == '__main__':
   app.run()
