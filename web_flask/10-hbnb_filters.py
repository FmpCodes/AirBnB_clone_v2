#!/usr/bin/python3
<<<<<<< HEAD

from models import storage
from flask import Flask, render_template

app = Flask('web_flask')


@app.route('/hbnb_filters', strict_slashes=False)
def display_filters():
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
=======
"""Starts a Flask web application"""

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Returns a rendered html template,
    using the web_static files
    """
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', **locals())


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
