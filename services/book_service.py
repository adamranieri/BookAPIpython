from abc import ABC, abstractmethod
from typing import List
from entities.book import Book


class BookService(ABC):

    @abstractmethod
    def register_book(self, book: Book) -> Book:
        pass

    @abstractmethod
    def retrieve_all_books(self) -> List[Book]:
        pass

    @abstractmethod
    def retrieve_book_by_id(self, book_id: int) -> Book:
        pass

    @abstractmethod
    def get_books_by_title(self, title: str) -> List[Book]:
        pass

    @abstractmethod
    def update_book(self, book: Book) -> Book:
        pass

    @abstractmethod
    def delete_book_by_id(self, book_id: int) -> bool:
        pass

    @abstractmethod
    def checkout_book(self, book_id: int) -> bool:
        pass

    @abstractmethod
    def checkin_book(self, book_id: int) -> bool:
        pass
