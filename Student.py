from dataclasses import dataclass, field
from typing import List
from datetime import datetime


@dataclass
class Student:
    """Student class"""

    user_id: str
    password: str
    borrowed_books: List = field(default_factory=list)

    def lendBookLibray(self, book, datatime):
        """Lend book to library and add and add the date after 30 days to the book to be lent"""
        self.borrowed_books.append({"book": book, "datatime": datatime})
        print(f"Book {book} lend")
