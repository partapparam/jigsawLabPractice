from models.book import Book 
import pytest

def test_book_creation():
    book = {'id': 1, 'title': 'Harry Potter', 'author_name': 'JK Rowling', 'published': 2005}
    book_obj = Book(**book)
    assert book_obj.id == book['id']
    assert book_obj.title == book['title']
    assert book_obj.author_name == book['author_name']