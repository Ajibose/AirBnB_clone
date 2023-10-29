#!/usr/bin/env python3

"""Unnitests for `models/engine/file_storage.py`"""

import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os


class TestFileStorage(unittest.TestCase):
    """Unittest for file storage"""

    def tearDown(self):
        """Rest json file"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        s = FileStorage()
        self.assertEqual(type(s), FileStorage)
        self.assertIsInstance(s, FileStorage)

    def test_storage_private_attr_dict(self):
        s = FileStorage()
        self.assertTrue(type(s.__class__._FileStorage__objects), dict)
        self.assertTrue(type(s.__class__._FileStorage__file_path), str)

    def test_new(self):
        a = Amenity()
        b = BaseModel()
        c = City()
        p = Place()
        r = Review()
        s = State()
        u = User()
        storage.new(a)
        storage.new(b)
        storage.new(c)
        storage.new(p)
        storage.new(p)
        storage.new(r)
        storage.new(s)
        storage.new(u)
        dic = FileStorage._FileStorage__objects
        self.assertIn(f"Amenity.{a.id}", dic.keys())
        self.assertTrue(type(dic[f"Amenity.{a.id}"]), "Amenity")
        self.assertIn(f"BaseModel.{b.id}", dic.keys())
        self.assertTrue(type(dic[f"BaseModel.{b.id}"]), "BaseModel")
        self.assertIn(f"City.{c.id}", dic.keys())
        self.assertTrue(type(dic[f"City.{c.id}"]), "City")
        self.assertIn(f"Place.{p.id}", dic.keys())
        self.assertTrue(type(dic[f"Place.{p.id}"]), "Place")
        self.assertIn(f"Review.{r.id}", dic.keys())
        self.assertTrue(type(dic[f"Review.{r.id}"]), "Review")
        self.assertIn(f"State.{s.id}", dic.keys())
        self.assertTrue(type(dic[f"State.{s.id}"]), "State")
        self.assertIn(f"User.{u.id}", dic.keys())
        self.assertTrue(type(dic[f"User.{u.id}"]), "User")

        u = User()
        u.id = 23
        u.name = "AirBnB"
        storage.new(u)

        self.assertIn(f"User.{u.id}", dic.keys())
        self.assertTrue(type(dic[f"User.{u.id}"]), "User")

    def test_all(self):
        dic = storage.all()
        self.assertEqual(type(dic), dict)
        self.assertEqual(dic, FileStorage._FileStorage__objects)

    def test_save(self):
        a = Amenity()
        b = BaseModel()
        c = City()
        p = Place()
        r = Review()
        s = State()
        u = User()
        storage.new(a)
        storage.new(b)
        storage.new(c)
        storage.new(p)
        storage.new(p)
        storage.new(r)
        storage.new(s)
        storage.new(u)
        storage.save()
        if os.path.exists(FileStorage._FileStorage__file_path):
            with open(FileStorage._FileStorage__file_path, "r") as f:
                json_dict = json.load(f)
        self.assertIn(f"Amenity.{a.id}", json_dict.keys())
        self.assertIn(f"BaseModel.{b.id}", json_dict.keys())
        self.assertIn(f"City.{c.id}", json_dict.keys())
        self.assertIn(f"Place.{p.id}", json_dict.keys())
        self.assertIn(f"Review.{r.id}", json_dict.keys())
        self.assertIn(f"State.{s.id}", json_dict.keys())
        self.assertIn(f"User.{u.id}", json_dict.keys())

    def test_save_with_args(self):
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload(self):
        dic = storage.all()
        self.assertFalse(dic)

        a = Amenity()
        b = BaseModel()
        c = City()
        p = Place()
        r = Review()
        s = State()
        u = User()

        storage.reload()

        self.assertIn(f"Amenity.{a.id}", dic.keys())
        self.assertIn(f"BaseModel.{b.id}", dic.keys())
        self.assertIn(f"City.{c.id}", dic.keys())
        self.assertIn(f"Place.{p.id}", dic.keys())
        self.assertIn(f"Review.{r.id}", dic.keys())
        self.assertIn(f"State.{s.id}", dic.keys())
        self.assertIn(f"User.{u.id}", dic.keys())

        FileStorage._FileStorage__file_path = "text.json"
        storage.reload()


if __name__ == "__main__":
    unittest.main()
