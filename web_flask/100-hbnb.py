#!/usr/bin/python3
<<<<<<< HEAD
=======
"""Starts a Flask web application"""
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59

from flask import Flask, render_template
from models import storage
<<<<<<< HEAD

app = Flask('web_flask')


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
=======
from models.state import State
from models.city import City
from models.amenity import Amenity
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a rendered html template,
    using the web_static files
    """
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    return render_template('100-hbnb.html', **locals())


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
