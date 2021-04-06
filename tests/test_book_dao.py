from daos.book_dao_postgres import BookDaoPostgres
from entities.book import Book

book_dao = BookDaoPostgres()
test_book = Book(0,'Dracula','Bram Stoker',True,2,0)

class TestBookDAO:

    def test_create_book(self):
        book_dao.create_book(test_book)
        assert test_book.book_id != 0

    def test_get_by_id(self):
        retrieved_book =book_dao.get_book_by_id(test_book.book_id)
        assert test_book.title == retrieved_book.title

    def test_update_book(self):
        test_book.available = False
        updated_book = book_dao.update_book(test_book)
        assert updated_book.available == test_book.available

    def test_delete_book(self):
        result = book_dao.delete_book_by_id(test_book.book_id)
        assert result == True
