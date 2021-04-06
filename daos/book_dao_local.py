from typing import List
from daos.book_dao import BookDAO
from entities.book import Book
from exceptions.resource_not_found import ResourceNotFound


class BookDaoLocal(BookDAO):

    id_maker = 0
    book_table = {}

    def create_book(self, book: Book) -> Book:
        BookDaoLocal.id_maker += 1
        book.book_id = BookDaoLocal.id_maker
        BookDaoLocal.book_table[book.book_id] = book
        return book

    def get_book_by_id(self, book_id: int) -> Book:
        try:
            book = BookDaoLocal.book_table[book_id]
            return book
        except KeyError as ke:
            raise ResourceNotFound(f'book with ID {book_id} was not found')


    def get_all_books(self) -> List[Book]:
        books = list(BookDaoLocal.book_table.values())
        return books

    def update_book(self, book: Book) -> Book:
        try:
            BookDaoLocal.book_table[book.book_id] = book
            return book
        except KeyError as e:
            raise ResourceNotFound(f'book with ID {book.book_id} was not found')

    def delete_book_by_id(self, book_id: int) -> bool:
        try:
            del BookDaoLocal.book_table[book_id]
            return True
        except KeyError as e:
            raise ResourceNotFound(f'book with ID {book_id} was not found')
