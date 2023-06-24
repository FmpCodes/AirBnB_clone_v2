<<<<<<< HEAD
tial script for undesrtand flask"""


from flask import Flask
=======
#!/usr/bin/python3
"""Starts a Flask web application"""
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
=======
def hello_holberton():
    """Returns a string at the root route"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
