from flask import Flask 
import psycopg2
from listing import Listing

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/listings')
def listings():
    conn = psycopg2.connect(database='test', user='param')
    cursor = conn.cursor()
    query = 'SELECT * from listings'
    cursor.execute(query)
    listings = cursor.fetchall()
    listings_objs = [Listing(listing).__dict__ for listing in listings]
    return listings

@app.route('/listings/<id>')
def listing_by_id(id):
    conn = psycopg2.connect(database='test', user='param')
    cursor = conn.cursor()
    query = 'SELECT * from listings where id = %s'
    cursor.execute(query, (id,))
    listing = cursor.fetchone()
    return Listing(listing).__dict__

app.run(debug=True)