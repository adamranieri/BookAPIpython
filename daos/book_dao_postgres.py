from typing import List
from daos.book_dao import BookDAO
from entities.book import Book
from utils.connection_util import connection


class BookDaoPostgres(BookDAO):

    def create_book(self, book: Book) -> Book:
        sql = """INSERT INTO book (title,author,available,return_date,book_condition) VALUES (%s,%s,%s,%s,%s) RETURNING book_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (book.title, book.author, book.available, 0, book.quality))
        connection.commit()
        book_id = cursor.fetchone()[0]
        book.book_id = book_id
        return book

    def get_book_by_id(self, book_id: int) -> Book:
        sql = """SELECT * from book WHERE book_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [book_id])
        records = cursor.fetchall()

        book_list = []

        for book in records:
            book = Book(book[0], book[5], book[1], book[2], book[3], book[4])
            book_list.append(book)

        return book_list[0]

    def get_all_books(self) -> List[Book]:
        sql = """SELECT * from book"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        book_list = []

        for book in records:
            book = Book(book[0], book[5], book[1], book[2], book[3], book[4])
            book_list.append(book)

        return book_list

    def update_book(self, book: Book) -> Book:
        sql = """UPDATE book SET title=%s,author=%s,available=%s,return_date=%s,book_condition=%s WHERE book_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, (book.title, book.author, book.available, book.return_date, book.quality, book.book_id))
        connection.commit()
        return book

    def delete_book_by_id(self, book_id: int) -> bool:
        sql = """DELETE FROM book WHERE book_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [book_id])
        connection.commit()
        return True