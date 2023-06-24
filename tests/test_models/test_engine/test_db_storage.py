#!/usr/bin/python3
<<<<<<< HEAD

import unittest
import pep8
from os import getenv
from models.base_model import BaseModel
=======
"""Defines unnittests for models/engine/db_storage.py."""
import pep8
import models
import MySQLdb
import unittest
from os import getenv
from models.base_model import Base
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
<<<<<<< HEAD
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
import models


class TestDBstorage(unittest.TestCase):
    """This will test de DB in mysql"""

    @classmethod
    def SetUpClass(cls):
        if type(models.storage) == DBStorage:
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()
            cls.user = User(email="abcd@holberton.com", password="betty")
            cls.storage._DBStorage__session.add(cls.user)
            cls.state = State(name="California")
            cls.storage._DBStorage__session.add(cls.state)
            cls.city = City(name="San_Francisco", state_id=cls.state.id)
            cls.storage._DBStorage__session.add(cls.city)
            cls.place = Place(city_id=cls.city.id, user_id=cls.uder.id, name="School")
            cls.storage._DBStorage__session.add(cls.place)
            cls.amenity = Amenity(name="Free_drinks")
            cls.storage._DBStorage__session.add(cls.amenity)
            cls.review = Review(place_id=cls.place.id, user_id=cls.user.id, text="Nice")
            cls.storage._DBStorage__session.add(cls.review)
            cls.storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(cls):
        """Delete test classes to reinitialize DBStorage session"""
        if type(models.storage) == DBStorage:
            cls.storage._DBStorage__session.delete(cls.user)
            cls.storage._DBStorage__session.delete(cls.state)
            cls.storage._DBStorage__session.delete(cls.city)
            cls.storage._DBStorage__session.delete(cls.amenity)
            cls.storage._DBStorage__session.delete(cls.place)
            cls.storage._DBStorage__session.delete(cls.review)
            cls.storage._DBStorage__session.commit()
            del cls.user
            del cls.state
            del cls.city
            del cls.place
            del cls.amenity
            del cls.review
            cls.storage._DBStorage__session.close()
            del cls.storage

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstr(self):
        """test docstrs."""
        self.assertIsNone(DBStorage.__doc__)
        self.assertIsNone(DBStorage.__init__.__doc__)
        self.assertIsNone(DBStorage.all.__doc__)
        self.assertIsNone(DBStorage.new.__doc__)
        self.assertIsNone(DBStorage.save.__doc__)
        self.assertIsNone(DBStorage.delete.__doc__)
        self.assertIsNone(DBStorage.reload.__doc__)

    @unittest.skipIf(type(models.storage) == FileStorage,"Test FS")
    def test_attr(self):
        self.assertTrue(isinstnce(self.storage._DBStorage__engine, Engine))
        self.assertTrue(isinstance(self.storage._DBStorage__session, Session))

    def test_met(self):
        self.assertTrue(hasattr(DBStorage, "__init__"))
        self.assertTrue(hasattr(DBStorage, "all"))
        self.assertTrue(hasattr(DBStorage, "new"))
        self.assertTrue(hasattr(DBStorage, "save"))
        self.assertTrue(hasattr(DBStorage, "delete"))
        self.assertTrue(hasattr(DBStorage, "reload"))

    @unittest.skipIf(type(models.storage) == FileStorage, "Test FS")
    def test_init(self):
        self.assertTrue(isinstance(self.storage, DBStorage))
=======
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59

    @unittest.skipIf(type(models.storage) == FileStorage, "Test FS")
    def test_all(self):
        obj = self.storage.all(State)
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 1)
        self.assertEqual(self.state, list(obj.values())[0])

<<<<<<< HEAD
    @unittest.skipIf(type(models.storage) == FileStorage, "Test FS")
    def test_new(self):
        cls = State(name="California")
        slef.storage.new(cls)
        store = list(self.storage._DBStrorage__session.new)
        self.assertIn(cls, store)

    @unittest.skipIf(type(models.storage) == FileStorage, "Test FS")
    def test_save(self):
        cls = State(name="Arizona")
        self.storage._DBStorage__session.add(cls)
        self.storage.save()
        db = MySQLdb.connect(user="hbnb_test",
                             passd="hbnb_test_pwd",
                             db="hbnb_test_db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE BINARY name = 'Arizona'")
        query = cursor.fetchall()
        self.assertEqual(1, len(query))
        self.assertEqual(cls.id, query[0][0])
        cursor.close()

    @unittest.skipIf(type(models.storage) == FileStorage, "Test FS")
    def test_reload(self):
        rl = self.storage._DBStorage__session
        self.storage.reload()
        self.assertIsInstance(self.storage.DBStorage__session, Session)
        self.assertNotEqual(rl, self.storage._DBStorage__session)
        self.storage._DBStorage__session.close()
        self.storage._DBStorage__session = rl

    @unittest.skipIf(type(models.storage) == FileStorage, "Test FS")
    def test_delete(self):
        cls = State(name="Texas")
        self.storage._DBStorage__session.add(cls)
        self.storage._DBStorage__session.commit()
        self.storage.delete(cls)
        self.assertIn(cls, list(self.storage._DBStorage__session.deleted))

    @unittest.skipIf(type(models.storage) == FileStorage, "Test FS")
    def test_none(self):
        try:
            self.storage.delete(None)
        except Exception:
            self.fail

=======
class TestDBStorage(unittest.TestCase):
    """Unittests for testing the DBStorage class."""

    @classmethod
    def setUpClass(cls):
        """DBStorage testing setup.
        Instantiate new DBStorage.
        Fill DBStorage test session with instances of all classes.
        """
        if type(models.storage) == DBStorage:
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()
            cls.state = State(name="California")
            cls.storage._DBStorage__session.add(cls.state)
            cls.city = City(name="San_Jose", state_id=cls.state.id)
            cls.storage._DBStorage__session.add(cls.city)
            cls.user = User(email="poppy@holberton.com", password="betty")
            cls.storage._DBStorage__session.add(cls.user)
            cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                              name="School")
            cls.storage._DBStorage__session.add(cls.place)
            cls.amenity = Amenity(name="Wifi")
            cls.storage._DBStorage__session.add(cls.amenity)
            cls.review = Review(place_id=cls.place.id, user_id=cls.user.id,
                                text="stellar")
            cls.storage._DBStorage__session.add(cls.review)
            cls.storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(cls):
        """DBStorage testing teardown.
        Delete all instantiated test classes.
        Clear DBStorage session.
        """
        if type(models.storage) == DBStorage:
            cls.storage._DBStorage__session.delete(cls.state)
            cls.storage._DBStorage__session.delete(cls.city)
            cls.storage._DBStorage__session.delete(cls.user)
            cls.storage._DBStorage__session.delete(cls.amenity)
            cls.storage._DBStorage__session.commit()
            del cls.state
            del cls.city
            del cls.user
            del cls.place
            del cls.amenity
            del cls.review
            cls.storage._DBStorage__session.close()
            del cls.storage

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_attributes(self):
        """Check for attributes."""
        self.assertTrue(isinstance(self.storage._DBStorage__engine, Engine))
        self.assertTrue(isinstance(self.storage._DBStorage__session, Session))

    def test_methods(self):
        """Check for methods."""
        self.assertTrue(hasattr(DBStorage, "__init__"))
        self.assertTrue(hasattr(DBStorage, "all"))
        self.assertTrue(hasattr(DBStorage, "new"))
        self.assertTrue(hasattr(DBStorage, "save"))
        self.assertTrue(hasattr(DBStorage, "delete"))
        self.assertTrue(hasattr(DBStorage, "reload"))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_init(self):
        """Test initialization."""
        self.assertTrue(isinstance(self.storage, DBStorage))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_all(self):
        """Test default all method."""
        obj = self.storage.all()
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 6)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_all_cls(self):
        """Test all method with specified cls."""
        obj = self.storage.all(State)
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 1)
        self.assertEqual(self.state, list(obj.values())[0])

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_new(self):
        """Test new method."""
        st = State(name="Washington")
        self.storage.new(st)
        store = list(self.storage._DBStorage__session.new)
        self.assertIn(st, store)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_save(self):
        """Test save method."""
        st = State(name="Virginia")
        self.storage._DBStorage__session.add(st)
        self.storage.save()
        db = MySQLdb.connect(user="hbnb_test",
                             passwd="hbnb_test_pwd",
                             db="hbnb_test_db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE BINARY name = 'Virginia'")
        query = cursor.fetchall()
        self.assertEqual(1, len(query))
        self.assertEqual(st.id, query[0][0])
        cursor.close()

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_delete(self):
        """Test delete method."""
        st = State(name="New_York")
        self.storage._DBStorage__session.add(st)
        self.storage._DBStorage__session.commit()
        self.storage.delete(st)
        self.assertIn(st, list(self.storage._DBStorage__session.deleted))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_delete_none(self):
        """Test delete method with None."""
        try:
            self.storage.delete(None)
        except Exception:
            self.fail

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_reload(self):
        """Test reload method."""
        og_session = self.storage._DBStorage__session
        self.storage.reload()
        self.assertIsInstance(self.storage._DBStorage__session, Session)
        self.assertNotEqual(og_session, self.storage._DBStorage__session)
        self.storage._DBStorage__session.close()
        self.storage._DBStorage__session = og_session

>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59

if __name__ == "__main__":
    unittest.main()
