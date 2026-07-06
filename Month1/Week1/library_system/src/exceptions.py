#Custom exceptions for the Library Management System.

class LibraryError(Exception):
    "Base exception for all library-related errors."
    pass

class BookNotFoundError(LibraryError):
    "Raised when a requested book does not exist in the library."
    pass

class NoCopiesAvailableError(LibraryError):
    "Raised when a book is out of stock."
    pass

class MemberNotFoundError(LibraryError):
    "Raised when a member ID cannot be found."
    pass

class BookAlreadyBorrowedError(LibraryError):
    "Raised when a member tries to borrow a copy they already have."
    pass

class BookNotBorrowedError(LibraryError):
    "Raised when a member tries to return a book they didn't borrow."
    pass