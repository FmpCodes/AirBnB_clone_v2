#!/usr/bin/python3
<<<<<<< HEAD

from flask import Flask
=======
"""Starts a Flask web application"""
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59

from flask import Flask
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
=======
    """Returns a string at the /hbnb route"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
