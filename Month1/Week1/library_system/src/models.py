"Data models representing core entities in the system."

from typing import List

class Book:
    def __init__(self, title: str, author: str, isbn: str, copies: int = 1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies_available = copies

    def to_dict(self) -> dict:
        """Serializes object state to a dictionary for JSON storage."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "copies_available": self.copies_available
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        "Factory method to instantiate an object from a dictionary."
        return cls(data["title"], data["author"], data["isbn"], data["copies_available"])

    def __repr__(self) -> str:
        return f"Book(ISBN={self.isbn}, Title='{self.title}', Available={self.copies_available})"

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) | Copies: {self.copies_available}"

class Member:
    def __init__(self, name: str, member_id: str, borrowed_isbns: List[str] = None):
        self.name = name
        self.member_id = member_id
        # Store ISBNs instead of full objects to avoid deeply nested/redundant JSON copies
        self.borrowed_books = borrowed_isbns if borrowed_isbns is not None else []

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Member':
        return cls(data["name"], data["member_id"], data["borrowed_books"])

    def __repr__(self) -> str:
        return f"Member(ID={self.member_id}, Name='{self.name}')"

    def __str__(self) -> str:
        return f"{self.name} [ID: {self.member_id}] | Books Borrowed: {len(self.borrowed_books)}"