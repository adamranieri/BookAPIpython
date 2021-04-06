from unittest.mock import MagicMock
from daos.book_dao_postgres import BookDaoPostgres
from entities.book import Book
from services.book_service_impl import BookServiceImpl

book1 = Book(0,'The Witcher','really hard last name',True,2,0)
book2 = Book(0,'The Catcher in the Rye','JD salinger',True,2,0)
book3 = Book(0,'Frankenstein','Mary Shelley',True,2,0)
books = [book1,book2,book3]

mock_book_dao = BookDaoPostgres()
mock_book_dao.get_all_books = MagicMock(return_value = books)
book_service = BookServiceImpl(mock_book_dao)

class TestBookService:

    def test_get_by_title_1(self):
        filtered_books = book_service.get_books_by_title('the')
        assert len(filtered_books) == 2

    def test_get_by_title_2(self):
        filtered_books = book_service.get_books_by_title('f')
        assert len(filtered_books) == 1
