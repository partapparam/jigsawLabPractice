from flask import Flask
import psycopg2
from src.models import Movie, Actor

def create_app(database, user):
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE=database,
        USER=user
    )

    @app.route('/movies')
    def all_movies():
        conn = psycopg2.connect(database=app.config['DATABASE'], user = app.config['USER'])
        cursor = conn.cursor()
        cursor.execute('select * from movies')
        movies = cursor.fetchall()
        movies_objects = [Movie(movie).__dict__ for movie in movies]
        return movies_objects

    @app.route('/movies/<id>')
    def movie_by_id(id):
        conn = psycopg2.connect(database=app.config['DATABASE'])
        cursor = conn.cursor()
        cursor.execute('select * from movies where id = %s', (id,))
        movie = cursor.fetchone()
        return Movie(movie).__dict__

    @app.route('/actors')
    def all_actors():
        conn = psycopg2.connect(database=app.config['DATABASE'], user = app.config['USER'])
        cursor = conn.cursor()
        cursor.execute('select * from actors')
        actors = cursor.fetchall()
        actors_objects = [Actor(actor).__dict__ for actor in actors]
        return actors_objects
    
    @app.route('/actors/<id>')
    def actor_by_id(id):
        conn = psycopg2.connect(database=app.config['DATABASE'], user = app.config['USER'])
        cursor = conn.cursor()
        cursor.execute('select * from actors where id = %s', (id,))
        actor = cursor.fetchone()
        return Actor(actor).__dict__
        
    return app