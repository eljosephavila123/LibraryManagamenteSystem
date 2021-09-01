from dataclasses import dataclass


@dataclass
class Book:
    """Book class"""

    code: str
    title: str
    author: str
    quantity: int

    def __str__(self):
        return f"{self.code}-{self.title}-{self.author}-{self.quantity}"
