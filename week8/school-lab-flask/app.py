import api as api
from settings import DB_NAME, DB_USER

app = api.create_app(DB_NAME, DB_USER, 'password')

if __name__ == '__main__':
    app.run(debug=True)