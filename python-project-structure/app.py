from settings import DATABASE, USER
from api import create_app

app = create_app(user=USER, database=DATABASE)

if __name__ == '__main__':
    app.run(debug=True)