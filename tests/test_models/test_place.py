#!/usr/bin/env python3
"""
    Unittests for module models/place,py
"""
import unittest
from models.place import Place
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage


class TestPlaceInstantiation(unittest.TestCase):
    """Test instantiation of Place class"""

    def setUp(self):
        """Reset the file"""
        dict = storage.all()
        dict.clear()
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_no_instantiation(self):
        a = Place()
        self.assertIsInstance(a, Place)
        self.assertIsInstance(a, BaseModel)
        self.assertTrue(issubclass(type(a), BaseModel))
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertTrue(hasattr(a, "created_at"))

    def test_with_no_args(self):
        a = Place()
        self.assertEqual(type(a.city_id), str)
        self.assertEqual(type(a.user_id), str)
        self.assertEqual(type(a.name), str)
        self.assertEqual(type(a.description), str)
        self.assertEqual(type(a.number_rooms), int)
        self.assertEqual(type(a.number_bathrooms), int)
        self.assertEqual(type(a.max_guest), int)
        self.assertEqual(type(a.price_by_night), int)
        self.assertEqual(type(a.latitude), float)
        self.assertEqual(type(a.longitude), float)
        self.assertEqual(type(a.amenity_ids), list)

    def test_attr_with_settr(self):
        c = Place()
        c.name = "Lagos"
        self.assertEqual(c.name, "Lagos")


if __name__ == "__main__":
    unittest.main()
