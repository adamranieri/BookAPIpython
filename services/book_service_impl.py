from typing import List
from daos.book_dao import BookDAO
from entities.book import Book
from services.book_service import BookService
from time import time


class BookServiceImpl(BookService):

    def __init__(self, book_dao: BookDAO):
        self.book_dao: BookDAO = book_dao

    def register_book(self, book: Book) -> Book:
        book.available = True
        book.return_date = 0
        return self.book_dao.create_book(book)

    def retrieve_all_books(self) -> List[Book]:
        return self.book_dao.get_all_books()

    def retrieve_book_by_id(self, book_id: int) -> Book:
        return self.book_dao.get_book_by_id(book_id)

    def get_books_by_title(self, title: str) -> List[Book]:
        books = self.book_dao.get_all_books()
        return [book for book in books if title.lower() in book.title.lower()]

    def update_book(self, book: Book) -> Book:
        self.book_dao.update_book(book)
        return book

    def delete_book_by_id(self, book_id: int) -> bool:
        self.book_dao.delete_book_by_id(book_id)
        return True

    def checkout_book(self, book_id: int) -> bool:
        book = self.book_dao.get_book_by_id(book_id)
        book.available = False
        book.return_date = int(time()+1209600)
        self.book_dao.update_book(book)
        return True

    def checkin_book(self, book_id: int) -> bool:
        book = self.book_dao.get_book_by_id(book_id)
        book.available = True
        book.return_date = 0
        self.update_book(book)
        return True
