import api as api
from settings import DB_NAME, DB_USER, PASSWORD

app = api.create_app(DB_NAME, DB_USER, PASSWORD)

if __name__ == '__main__':
    app.run(debug=True)