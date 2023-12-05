import psycopg2 
from flask import Flask
from players import Player

app = Flask(__name__)

# here we take our players data and make models to return for each Player
@app.route('/players')
def players():
    conn = psycopg2.connect(database='flask', user='param', password='postgres')
    cursor = conn.cursor()
    cursor.execute('select * from players')
    player_records = cursor.fetchall()
    players = [Player(player_record) for player_record in player_records]
    player_dicts = [player.__dict__ for player in players]
    return player_dicts

if __name__ == "__main__":
    app.run(debug = True)


