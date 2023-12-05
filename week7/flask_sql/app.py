import psycopg2 
from flask import Flask

app = Flask(__name__)

@app.route('/players')
def players():
    conn = psycopg2.connect(database='flask', user='param', password='postgres')
    cursor = conn.cursor()
    cursor.execute('select * from players')
    players = cursor.fetchall()
    return players

app.run(debug = True)


