from models.author import Author
import pytest 

# test that an Author can be created
def test_author_creation():
    author = {'id': 1, 'work_count': 10, 'name': 'JK Rowling'}
    author_obj = Author(**author)
    assert author_obj.name == author['name']
    assert author_obj.id == author['id']
    assert author_obj.work_count == author['work_count']
    