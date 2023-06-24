#!/usr/bin/python3
<<<<<<< HEAD
"""test for file storage"""
import unittest
import pep8
import json
import os
=======
"""Defines unnittests for models/engine/file_storage.py."""
import os
import json
import pep8
import unittest
from datetime import datetime
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
<<<<<<< HEAD
    '''this will test the FileStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""

        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.storage = FileStorage()
        cls.base = BaseModel()
        key = "{}.{}".format(type(cls.base).__name__, cls.base.id)
        FileStorage._FileStorage__objects[key] = cls.base
        cls.user = User()
        key = "{}.{}".format(type(cls.user).__name__, cls.user.id)
        FileStorage._FileStorage__objects[key] = cls.user
        cls.state = State()
        key = "{}.{}".format(type(cls.state).__name__, cls.state.id)
        FileStorage._FileStorage__objects[key] = cls.state
        cls.city = City()
        key = "{}.{}".format(type(cls.city).__name__, cls.city.id)
        FileStorage._FileStorage__objects[key] = cls.city
        cls.amenity = Amenity()
        key = "{}.{}".format(type(cls.amenity).__name__, cls.amenity.id)
        FileStorage._FileStorage__objects[key] = cls.amenity
        cls.place = Place()
        key = "{}.{}".format(type(cls.place).__name__, cls.place.id)
        FileStorage._FileStorage__objects[key] = cls.place
        cls.review = Review()
        key = "{}.{}".format(type(cls.review).__name__, cls.review.id)
        FileStorage._FileStorage__objects[key] = cls.review

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        try:
=======
    """Unittests for testing the FileStorage class."""

    @classmethod
    def setUpClass(cls):
        """FileStorage testing setup.
        Temporarily renames any existing file.json.
        Resets FileStorage objects dictionary.
        Creates instances of all class types for testing.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.storage = FileStorage()
        cls.base = BaseModel()
        key = "{}.{}".format(type(cls.base).__name__, cls.base.id)
        FileStorage._FileStorage__objects[key] = cls.base
        cls.user = User()
        key = "{}.{}".format(type(cls.user).__name__, cls.user.id)
        FileStorage._FileStorage__objects[key] = cls.user
        cls.state = State()
        key = "{}.{}".format(type(cls.state).__name__, cls.state.id)
        FileStorage._FileStorage__objects[key] = cls.state
        cls.place = Place()
        key = "{}.{}".format(type(cls.place).__name__, cls.place.id)
        FileStorage._FileStorage__objects[key] = cls.place
        cls.city = City()
        key = "{}.{}".format(type(cls.city).__name__, cls.city.id)
        FileStorage._FileStorage__objects[key] = cls.city
        cls.amenity = Amenity()
        key = "{}.{}".format(type(cls.amenity).__name__, cls.amenity.id)
        FileStorage._FileStorage__objects[key] = cls.amenity
        cls.review = Review()
        key = "{}.{}".format(type(cls.review).__name__, cls.review.id)
        FileStorage._FileStorage__objects[key] = cls.review

    @classmethod
    def tearDownClass(cls):
        """FileStorage testing teardown.
        Restore original file.json.
        Delete all test class instances.
        """
        try:
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.storage
        del cls.base
        del cls.user
        del cls.state
<<<<<<< HEAD
        del cls.city
        del cls.place
=======
        del cls.place
        del cls.city
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
        del cls.amenity
        del cls.review

    def test_pep8_FileStorage(self):
<<<<<<< HEAD
        """Tests pep8 style"""
=======
        """Test pep8 styling."""
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

<<<<<<< HEAD
    def test_attr(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_hasattr(self):
=======
    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.delete.__doc__)

    def test_attributes(self):
        """Check for attributes."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_methods(self):
        """Check for methods."""
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "reload"))
        self.assertTrue(hasattr(FileStorage, "delete"))

<<<<<<< HEAD
    def test_docstr(self):
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.delete.__doc__)

    def test_all(self):
        """tests if all works in File Storage"""
        obj = self.storage.all()
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, FileStorage._FileStorage__objects)

    def test_new(self):
        """test when new is created"""
        BModel = BaseModel()
        self.storage.new(BModel)
        storag = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + BModel.id, storag.keys())
        self.assertIn(self.base, storag.values())

    def test_reload_filestorage(self):
        """
        tests reload
        """
        BModel = BaseModel()
        with open("file.json", "w", encoding="utf-8") as f:
            key = "{}.{}".format(type(BModel).__name__, BModel.id)
            json.dump({key: BModel.to_dict()}, f)
        self.storage.reload()
        storag = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + BModel.id, storag)

    def test_delete(self):
        BModel = BaseModel()
        key = "{}.{}".format(type(BModel).__name__, BModel.id)
        FileStorage._FileStorage__objects[key] = BModel
        self.storage.delete(BModel)
        self.assertNotIn(BModel, FileStorage._FileStorage__objects)

    def test_save(self):
        self.storage.save()
        with open("file.json", "r", encoding="utf-8") as f:
            saves = f.read()
            self.assertIn("BaseModel." + self.base.id, saves)
            self.assertIn("User." + self.user.id, saves)
            self.assertIn("Place." + self.place.id, saves)
            self.assertIn("State." + self.state.id, saves)
            self.assertIn("City." + self.city.id, saves)
            self.assertIn("Review." + self.review.id, saves)
            self.assertIn("Amenity." + self.amenity.id, saves)
=======
    def test_init(self):
        """Test initialization."""
        self.assertTrue(isinstance(self.storage, FileStorage))

    def test_all(self):
        """Test default all method."""
        obj = self.storage.all()
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, FileStorage._FileStorage__objects)
        self.assertEqual(len(obj), 7)

    def test_all_cls(self):
        """Test all method with specified cls."""
        obj = self.storage.all(BaseModel)
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 1)
        self.assertEqual(self.base, list(obj.values())[0])

    def test_new(self):
        """Test new method."""
        bm = BaseModel()
        self.storage.new(bm)
        store = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, store.keys())
        self.assertIn(self.base, store.values())

    def test_save(self):
        """Test save method."""
        self.storage.save()
        with open("file.json", "r", encoding="utf-8") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + self.base.id, save_text)
            self.assertIn("User." + self.user.id, save_text)
            self.assertIn("State." + self.state.id, save_text)
            self.assertIn("Place." + self.place.id, save_text)
            self.assertIn("City." + self.city.id, save_text)
            self.assertIn("Amenity." + self.amenity.id, save_text)
            self.assertIn("Review." + self.review.id, save_text)

    def test_reload(self):
        """Test reload method."""
        bm = BaseModel()
        with open("file.json", "w", encoding="utf-8") as f:
            key = "{}.{}".format(type(bm).__name__, bm.id)
            json.dump({key: bm.to_dict()}, f)
        self.storage.reload()
        store = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, store)

    def test_reload_no_file(self):
        """Test reload method with no existing file.json."""
        try:
            self.storage.reload()
        except Exception:
            self.fail

    def test_delete(self):
        """Test delete method."""
        bm = BaseModel()
        key = "{}.{}".format(type(bm).__name__, bm.id)
        FileStorage._FileStorage__objects[key] = bm
        self.storage.delete(bm)
        self.assertNotIn(bm, FileStorage._FileStorage__objects)

    def test_delete_nonexistant(self):
        """Test delete method with a nonexistent object."""
        try:
            self.storage.delete(BaseModel())
        except Exception:
            self.fail
>>>>>>> d45487f8b7bb0f169ae648792a5c27416139bc59


if __name__ == "__main__":
    unittest.main()
