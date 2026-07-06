import os
import json
from typing import Dict, Optional
from src.models import Book, Member
from src.exceptions import (
    BookNotFoundError, NoCopiesAvailableError, MemberNotFoundError,
    BookAlreadyBorrowedError, BookNotBorrowedError
)

class Library:
    def __init__(self, storage_path: str = "data/library_storage.json"):
        self.storage_path = storage_path
        # Efficient O(1) indexing lookup tables
        self.books: Dict[str, Book] = {}       # Key: isbn
        self.members: Dict[str, Member] = {}   # Key: member_id
        
        self._load_data()

    def add_book(self, title: str, author: str, isbn: str, copies: int = 1) -> None:
        "Adds new copies to an existing book, or provisions a new book profile."
        if isbn in self.books:
            self.books[isbn].copies_available += copies
        else:
            self.books[isbn] = Book(title, author, isbn, copies)
        self._save_data()

    def register_member(self, name: str, member_id: str) -> None:
        "Registers a new library member if the ID is unique."
        if member_id in self.members:
            print(f"\n[!] Notice: Member ID {member_id} is already taken.")
            return
        self.members[member_id] = Member(name, member_id)
        self._save_data()

    def search_book(self, query: str) -> list[Book]:
        "Searches books dynamically matching title or author fragments."
        query_lower = query.lower()
        return [
            book for book in self.books.values()
            if query_lower in book.title.lower() or query_lower in book.author.lower() or query_lower == book.isbn
        ]

    def issue_book(self, member_id: str, isbn: str) -> None:
        "Validates boundaries and processes a book checkout transaction."
        if member_id not in self.members:
            raise MemberNotFoundError(f"Member ID '{member_id}' does not exist.")
        if isbn not in self.books:
            raise BookNotFoundError(f"Book with ISBN '{isbn}' does not exist.")
        
        member = self.members[member_id]
        book = self.books[isbn]

        if isbn in member.borrowed_books:
            raise BookAlreadyBorrowedError(f"Member already holds a copy of '{book.title}'.")
        if book.copies_available <= 0:
            raise NoCopiesAvailableError(f"No available copies remaining for '{book.title}'.")

        # Transaction execution
        book.copies_available -= 1
        member.borrowed_books.append(isbn)
        self._save_data()

    def return_book(self, member_id: str, isbn: str) -> None:
        "Processes a book return transaction safely updating library inventory."
        if member_id not in self.members:
            raise MemberNotFoundError(f"Member ID '{member_id}' does not exist.")
        if isbn not in self.books:
            raise BookNotFoundError(f"Book with ISBN '{isbn}' does not exist.")

        member = self.members[member_id]
        book = self.books[isbn]

        if isbn not in member.borrowed_books:
            raise BookNotBorrowedError(f"Member did not borrow '{book.title}'.")

        # Transaction execution
        book.copies_available += 1
        member.borrowed_books.remove(isbn)
        self._save_data()

    def _save_data(self) -> None:
        "Serializes current memory state safely into JSON file system."
        # Ensure directory infrastructure exists
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        
        payload = {
            "books": {isbn: book.to_dict() for isbn, book in self.books.items()},
            "members": {m_id: member.to_dict() for m_id, member in self.members.items()}
        }
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(payload, f, indent=4)

    def _load_data(self) -> None:
        "Hydrates runtime collections from local storage if available."
        if not os.path.exists(self.storage_path):
            return

        try:
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                payload = json.load(f)
                
                self.books = {
                    isbn: Book.from_dict(raw) 
                    for isbn, raw in payload.get("books", {}).items()
                }
                self.members = {
                    m_id: Member.from_dict(raw) 
                    for m_id, raw in payload.get("members", {}).items()
                }
        except (json.JSONDecodeError, KeyError):
            print("Warning: Corrupted storage found. Instantiating a clean database infrastructure.")
            self.books, self.members = {}, {}