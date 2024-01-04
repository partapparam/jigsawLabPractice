# search artist URL
# https://api.spotify.com/v1/search?q=adele&type=artist

from flask import Flask 
from models.client import ApiClient
from models.book_adapter import BookAdapter

app = Flask(__name__)

@app.route('/author/<author>')
def artist(author):
    client = ApiClient(URL=f'https://openlibrary.org/search/authors.json?q={author}')
    response = client.run()
    books = BookAdapter().run(response.docs)
    return response
author = 'Kevin Wilson'
client = ApiClient(URL=f'https://openlibrary.org/search/authors.json?q={author}')
response = client.run()
# books = BookAdapter().run(response['docs'])


