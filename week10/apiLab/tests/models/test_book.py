from models.book import Book 
from models.book_adapter import BookAdapter
import pytest

def test_book_creation() -> None:
    book: dict = {'id': 1, 'title': 'Harry Potter', 'author_name': 'JK Rowling', 'published': 2005}
    book_obj = Book(**book)
    assert book_obj.id == book['id']
    assert book_obj.title == book['title']
    assert book_obj.author_name == book['author_name']

def test_select_attributes()-> None:
    book: dict = {'key': 1, 'title': 'Harry Potter', 'author_name': 'JK Rowling', 'first_publish_year': 2005, 'ISBN': 12423414, 'publisher': 'Penguin'}
    book_attrs: dict = BookAdapter().select_attributes(book=book)
    assert book_attrs['id'] == book['key']
    assert book_attrs['published'] == book['first_publish_year']

def test_run():
    pass