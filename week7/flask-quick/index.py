from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/players/<name>')
def show_player(name):
    return f'Welcome to the page of: <h1> {name} </h1>'

@app.route('/try')
def show_test():
    return 'The reload works'

@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name=name)

@app.route('/player/<name>')
def player(name):
    return render_template('player.html', name=name)

@app.route('/restaurants')
def restaurants():
    return render_template('restaurants.html')

@app.route('/restaurants/<name>')
def restaurant_name(name):
    return render_template('restaurant_name.html', name=name)


app.run(debug = True)