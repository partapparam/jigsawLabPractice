from flask import Flask

def create_app(database, user, password):
    app = Flask(__name__)
    app.config['DB_NAME'] = database
    app.config['DB_USER'] = user
    app.config['PASSWORD'] = password


    @app.route('/')
    def home():
        return 'Hello World'
    


    return app