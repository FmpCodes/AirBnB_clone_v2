#!/usr/bin/python3
<<<<<<< HEAD

from flask import Flask
from flask import render_template
=======
"""Starts a Flask web application"""
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hello():
    return "Hello HBNB!"
=======
def hello_holberton():
    """Returns a string at the root route"""
    return 'Hello HBNB!'
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    txt = text.replace('_', " ")
    return "C {}". format(txt)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    txt = text.replace('_', " ")
    return "Python {}". format(txt)
=======
    """Returns a string at the /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Returns a string at the /c/<text> route,
    expands the <text> variable"""
    new = text.replace('_', ' ')
    return 'C %s' % new


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text):
    """Returns a string at the /python route, with a default text
    of 'is cool', or the expansion of <text>"""
    new = text.replace('_', ' ')
    return 'Python %s' % new
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
<<<<<<< HEAD
    return '{} is a number'.format(n)
=======
    """Returns a string at the /number/<n> route,
    only if n is an int"""
    if type(n) == int:
        return '%i is a number' % n
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
<<<<<<< HEAD
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
=======
    """Returns a template at the /number_template/<n> route,
    expanding route"""
    if type(n) == int:
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
