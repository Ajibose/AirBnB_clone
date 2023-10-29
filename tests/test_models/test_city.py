#!/usr/bin/python3
"""
    Unittests for module models/city,py
"""
import unittest
from models.city import City
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage


class TestCityInstantiation(unittest.TestCase):
    """Test instantiation of city class"""

    def setUp(self):
        """Reset the file"""
        dict = storage.all()
        dict.clear()
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_no_args(self):
        a = City()
        self.assertIsInstance(a, City)
        self.assertIsInstance(a, BaseModel)
        self.assertTrue(issubclass(type(a), BaseModel))
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertTrue(hasattr(a, "created_at"))

    def test_with_settr(self):
        a = City()
        a.name = "Lagos"
        a.state_id = "+234LA"
        self.assertTrue(hasattr(a, "name"))
        self.assertEqual(a.name, "Lagos")
        self.assertTrue(hasattr(a, "state_id"))
        self.assertEqual(a.state_id, "+234LA")

    def test_attr_with_default(self):
        c = City()
        self.assertEqual(c.name, "")
        self.assertEqual(c.state_id, "")
        self.assertEqual(type(c.name), str)
        self.assertEqual(type(c.state_id), str)


if __name__ == "__main__":
    unittest.main()
