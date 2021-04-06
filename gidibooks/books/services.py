from typing import List, Dict

from books.models import Book

from users.models import User


def find_book(data: List):
    """
    Uses Queryset filter to find book that fit items
    in the argument. Converts the response to dictionary
    """
    pass


def my_borrowed_books(user_id: str):
    """
    Uses Queryset filter to find book that fit user_id.
    Converts the response to dictionary
    """
    pass


def borrow(data: Dict):
    """
    Data contains user_id and list[book_ids]
    Queryset finds books with the given IDS
    and updates their status to pending and
    borrower to user
    """
    pass
