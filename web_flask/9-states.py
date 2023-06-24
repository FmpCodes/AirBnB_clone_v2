#!/usr/bin/python3
<<<<<<< HEAD

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
=======
"""Starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_1(id=None):
    """Returns a rendered html template:
    if id is given, list the cities of that State
    else, list all States
    """
    states = storage.all('State')
    if id:
        key = '{}.{}'.format('State', id)
        if key in states:
            states = states[key]
        else:
            states = None
    else:
        states = storage.all('State').values()
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
