from entities.book import Book
from abc import ABC, abstractmethod
from typing import List


class BookDAO(ABC):

    @abstractmethod
    def create_book(self, book: Book) -> Book:
        pass

    @abstractmethod
    def get_book_by_id(self, book_id: int) -> Book:
        pass

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass

    @abstractmethod
    def update_book(self, book: Book) -> Book:
        pass

    @abstractmethod
    def delete_book_by_id(self, book_id: int) -> bool:
        pass
