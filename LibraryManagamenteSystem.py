from tabulate import tabulate
from dataclasses import dataclass, field
from typing import List
from colors import bcolors


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


@dataclass
class LibraryManagamenteSystem(metaclass=SingletonMeta):
    """Library Managamente System Class"""

    list_of_books: List = field(default_factory=list)
    list_of_book_not_available: List = field(default_factory=list)

    def displayAvabileBooks(self):
        """Show available books"""
        print(f"{bcolors.BOLD}{bcolors.HEADER}Avabile Books:{bcolors.ENDC}")
        print("=" * 60)
        table = []
        for book in self.list_of_books:
            table.append([book.code, book.title, book.author, book.quantity])
        print(tabulate(table, headers=["Code", "Title", "Author", "Quantity"]))
        print("=" * 60)

    def displayNotAvabileBooks(self):
        """Show borrowed books"""
        print(f"{bcolors.BOLD}{bcolors.HEADER}Lend Books:{bcolors.ENDC}")
        print("=" * 60)
        table = []
        for book in self.list_of_book_not_available:
            table.append([book.code, book.title, book.author, book.quantity])
        print(tabulate(table, headers=["Code", "Title", "Author", "Quantity"]))
        print("=" * 60)

    def addBook(self, book):
        """[Add book to library ]
        Args:
            book ([Book]): [The book to be added]
        Returns:
            [Book]: [If the book is added]
        """
        if book not in self.list_of_books:
            self.list_of_books.append(book)
            print(f"{bcolors.BOLD}{bcolors.OKGREEN}Book {book} added{bcolors.ENDC}")

    def addBookExisting(self, code_id, quantity=1):
        """[When a book is added, if it already exists in the database , it increases by 1]

        Args:
            code_id ([str]): [The book code]
            quantity (int, optional): [Quantity increase]. Defaults to 1.

        Returns:
            [Book]: [If the book is found]
        """
        for book in self.list_of_books:
            if book.code == code_id:
                book.quantity += quantity
                print(f"{bcolors.BOLD}{bcolors.OKGREEN}Book {book} added{bcolors.ENDC}")
                return book
        return None

    def lendBookStudent(self, book):
        """[Add to a list of borrowed books]

        Args:
            book ([Book]): [The book to be lent]

        Returns:
            [Book: [The lent book]
        """
        if book in self.list_of_books:
            if book.quantity > 0:
                book.quantity -= 1
            self.list_of_book_not_available.append(book)
            print(f"{bcolors.BOLD}{bcolors.OKGREEN}Book {book} lend{bcolors.ENDC}")
            return book
        print("Book not found")

    def findBook(self, code_id):
        """[Find a book by code]
        Args:
            code_id ([str]): [The book code]
        Returns:
            [Book]: [If the book is found]
        """
        for book in self.list_of_books:
            if book.code == code_id:
                return book
        return None
