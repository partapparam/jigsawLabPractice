# search artist URL
# https://api.spotify.com/v1/search?q=adele&type=artist

from flask import Flask 
from models.client import ApiClient
from models.author_adapter import AuthorAdapter
from models.book_adapter import BookAdapter
from models.author import Author
from models.book import Book

app = Flask(__name__)

@app.route('/author/<author>')
def author(author) -> list[dict]:
    client = ApiClient(URL=f'https://openlibrary.org/search/authors.json?q={author}')
    response: dict = client.run()
    authors: list[Author] = AuthorAdapter().run(authors=response['docs'])
    author_dicts: list[dict] = [author.__dict__ for author in authors] 
    return author_dicts

@app.route('/author/works/<author>')
def works(author) -> list[dict]:
    client = ApiClient(URL=f'https://openlibrary.org/search.json?q={author}&sort=new')
    response: dict = client.run()
    books: list[Book] = BookAdapter().run(books=response['docs'])
    book_dicts: list[dict] = [book.__dict__ for book in books] 
    return book_dicts
