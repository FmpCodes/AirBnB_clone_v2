#!/usr/bin/python3
<<<<<<< HEAD
"""create a unique FileStorage instance for your application
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
=======
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
