#!/usr/bin/python3
<<<<<<< HEAD
"""test for review"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):
    """this will test the place class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "The srongest in the Galaxy"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.rev

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Review(self):
        """checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """chekcing if review have attributes"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_is_subclass_Review(self):
        """test if review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_attribute_types_Review(self):
        """test attribute type for Review"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    def test_save_Review(self):
        """test if the save works"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict_Review(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.rev), True)
=======
"""Defines unnittests for models/review.py."""
import os
import pep8
import models
import MySQLdb
import unittest
from datetime import datetime
from models.base_model import Base
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker


class TestReview(unittest.TestCase):
    """Unittests for testing the Review class."""

    @classmethod
    def setUpClass(cls):
        """Review testing setup.
        Temporarily renames any existing file.json.
        Resets FileStorage objects dictionary.
        Creates FileStorage, DBStorage and Review instances for testing.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.filestorage = FileStorage()
        cls.state = State(name="California")
        cls.city = City(name="San Francisco", state_id=cls.state.id)
        cls.user = User(email="poppy@holberton.com", password="betty98")
        cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                          name="Betty")
        cls.review = Review(text="stellar", place_id=cls.place.id,
                            user_id=cls.user.id)

        if type(models.storage) == DBStorage:
            cls.dbstorage = DBStorage()
            Base.metadata.create_all(cls.dbstorage._DBStorage__engine)
            Session = sessionmaker(bind=cls.dbstorage._DBStorage__engine)
            cls.dbstorage._DBStorage__session = Session()

    @classmethod
    def tearDownClass(cls):
        """Review testing teardown.
        Restore original file.json.
        Delete the FileStorage, DBStorage and Review test instances.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.state
        del cls.city
        del cls.user
        del cls.place
        del cls.review
        del cls.filestorage
        if type(models.storage) == DBStorage:
            cls.dbstorage._DBStorage__session.close()
            del cls.dbstorage

    def test_pep8(self):
        """Test pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/review.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        """Check for attributes."""
        us = Review(email="a", password="a")
        self.assertEqual(str, type(us.id))
        self.assertEqual(datetime, type(us.created_at))
        self.assertEqual(datetime, type(us.updated_at))
        self.assertTrue(hasattr(us, "text"))
        self.assertTrue(hasattr(us, "place_id"))
        self.assertTrue(hasattr(us, "user_id"))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_nullable_attributes(self):
        """Test that email attribute is non-nullable."""
        with self.assertRaises(OperationalError):
            self.dbstorage._DBStorage__session.add(Review(
                place_id=self.place.id, user_id=self.user.id))
            self.dbstorage._DBStorage__session.commit()
        self.dbstorage._DBStorage__session.rollback()
        with self.assertRaises(OperationalError):
            self.dbstorage._DBStorage__session.add(Review(
                text="a", user_id=self.user.id))
            self.dbstorage._DBStorage__session.commit()
        self.dbstorage._DBStorage__session.rollback()
        with self.assertRaises(OperationalError):
            self.dbstorage._DBStorage__session.add(Review(
                text="a", place_id=self.place.id))
            self.dbstorage._DBStorage__session.commit()

    def test_is_subclass(self):
        """Check that Review is a subclass of BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_init(self):
        """Test initialization."""
        self.assertIsInstance(self.review, Review)

    def test_two_models_are_unique(self):
        """Test that different Review instances are unique."""
        us = Review(email="a", password="a")
        self.assertNotEqual(self.review.id, us.id)
        self.assertLess(self.review.created_at, us.created_at)
        self.assertLess(self.review.updated_at, us.updated_at)

    def test_init_args_kwargs(self):
        """Test initialization with args and kwargs."""
        dt = datetime.utcnow()
        st = Review("1", id="5", created_at=dt.isoformat())
        self.assertEqual(st.id, "5")
        self.assertEqual(st.created_at, dt)

    def test_str(self):
        """Test __str__ representation."""
        s = self.review.__str__()
        self.assertIn("[Review] ({})".format(self.review.id), s)
        self.assertIn("'id': '{}'".format(self.review.id), s)
        self.assertIn("'created_at': {}".format(
            repr(self.review.created_at)), s)
        self.assertIn("'updated_at': {}".format(
            repr(self.review.updated_at)), s)
        self.assertIn("'text': '{}'".format(self.review.text), s)
        self.assertIn("'place_id': '{}'".format(self.review.place_id), s)
        self.assertIn("'user_id': '{}'".format(self.review.user_id), s)

    @unittest.skipIf(type(models.storage) == DBStorage,
                     "Testing DBStorage")
    def test_save_filestorage(self):
        """Test save method with FileStorage."""
        old = self.review.updated_at
        self.review.save()
        self.assertLess(old, self.review.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("Review." + self.review.id, f.read())

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_save_dbstorage(self):
        """Test save method with DBStorage."""
        old = self.review.updated_at
        self.state.save()
        self.city.save()
        self.user.save()
        self.place.save()
        self.review.save()
        self.assertLess(old, self.review.updated_at)
        db = MySQLdb.connect(user="hbnb_test",
                             passwd="hbnb_test_pwd",
                             db="hbnb_test_db")
        cursor = db.cursor()
        cursor.execute("SELECT * \
                          FROM `reviews` \
                         WHERE BINARY text = '{}'".
                       format(self.review.text))
        query = cursor.fetchall()
        self.assertEqual(1, len(query))
        self.assertEqual(self.review.id, query[0][0])
        cursor.close()

    def test_to_dict(self):
        """Test to_dict method."""
        review_dict = self.review.to_dict()
        self.assertEqual(dict, type(review_dict))
        self.assertEqual(self.review.id, review_dict["id"])
        self.assertEqual("Review", review_dict["__class__"])
        self.assertEqual(self.review.created_at.isoformat(),
                         review_dict["created_at"])
        self.assertEqual(self.review.updated_at.isoformat(),
                         review_dict["updated_at"])
        self.assertEqual(self.review.text, review_dict["text"])
        self.assertEqual(self.review.place_id, review_dict["place_id"])
        self.assertEqual(self.review.user_id, review_dict["user_id"])
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59


if __name__ == "__main__":
    unittest.main()
