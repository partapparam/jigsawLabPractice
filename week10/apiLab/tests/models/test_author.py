from models.author import Author
from models.author_adapter import AuthorAdapter
import pytest 

# test that an Author can be created
def test_author_creation() -> None:
    author: dict = {'id': 1, 'work_count': 10, 'name': 'JK Rowling'}
    author_obj = Author(**author)
    assert author_obj.name == author['name']
    assert author_obj.id == author['id']
    assert author_obj.work_count == author['work_count']

def test_select_attributes() -> None:
    author: dict = {'key': 1, 'work_count': 10, 'name': 'JK Rowling', 'school': 'USC'}
    author_attrs: dict = AuthorAdapter().select_attributes(author=author)
    assert author_attrs['id'] == author['key']

def test_run() -> None:
    authors: list[dict] = [{'key': 1, 'work_count': 10, 'name': 'JK Rowling'}, {'key': 2, 'work_count': 20, 'name': 'Kevin Wilson'}]

    adapted_authors_list: list[Author] = AuthorAdapter().run(authors=authors)
    assert len(adapted_authors_list) == 2
    assert adapted_authors_list[0].name == 'JK Rowling'
    assert adapted_authors_list[1].name == 'Kevin Wilson'