class Book:

    def __init__(self, book_id: int, title: str, author: str, available: bool, quality: int, return_date: int):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available
        self.quality = quality
        self.return_date = return_date

    def json(self):
        return {'bookId': self.book_id,
                'title': self.title,
                'author': self.author,
                'available': self.available,
                'quality': self.quality,
                'returnDate': self.return_date
                }

    @staticmethod
    def json_deserialize(json):
        book = Book(0, '', '', False, 0, 0)
        book.book_id = json["bookId"]
        book.title = json['title']
        book.author = json['author']
        book.available = json['available']
        book.quality = json['quality']
        book.return_date = json['returnDate']
        return book
