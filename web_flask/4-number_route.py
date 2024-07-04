#!/usr/bin/python3
"""documentation importing Flask"""
from flask import Flask
"""documentation calling flask"""
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """function to return Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """function to return HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c_isfun(text):
    """function to return C"""
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>',)
def python(text="is cool"):
    """function to return python"""
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'


@app.route('/number/<int:n>')
def number(n):
    """function to return a number"""
    return f"{n} is a number"


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
