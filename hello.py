from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/about/')
def about():
    return 'This is a Flask website'


@app.route('/hello/')
def hello():
    return 'Hello'

@app.route('/add/2/2/')
def twoplustwo():
    return '2+2'

@app.route('/circle/<radius>/')
def circle_area(radius):
    radius = int(radius)
    area = 3.14 * (radius ** 2)
    return str(area)


app.run(debug=True)

