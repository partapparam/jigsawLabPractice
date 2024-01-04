# search artist URL
# https://api.spotify.com/v1/search?q=adele&type=artist

from flask import Flask 
from models.client import ApiClient
from models.author_adapter import AuthorAdapter
from models.book_adapter import BookAdapter

app = Flask(__name__)

@app.route('/author/<author>')
def author(author):
    client = ApiClient(URL=f'https://openlibrary.org/search/authors.json?q={author}')
    response = client.run()
    authors = AuthorAdapter().run(response['docs'])
    author_dicts = [author.__dict__ for author in authors] 
    return author_dicts

@app.route('/author/works/<author>')
def works(author):
    client = ApiClient(URL=f'https://openlibrary.org/search.json?q={author}&sort=new')
    response = client.run()
    books = BookAdapter().run(response['docs'])
    book_dicts = [book.__dict__ for book in books] 
    return book_dicts
