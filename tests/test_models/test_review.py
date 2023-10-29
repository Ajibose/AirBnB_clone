#!/usr/bin/env python3
"""
    Unittests for module models/review,py
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage


class TestReviewInstantiation(unittest.TestCase):
    """Test instantiation of Review class"""

    def setUp(self):
        """Reset the file"""
        dict = storage.all()
        dict.clear()
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_no_args(self):
        a = Review()
        self.assertIsInstance(a, Review)
        self.assertTrue(issubclass(type(a), BaseModel))
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertTrue(hasattr(a, "created_at"))

    def test_with_no_args(self):
        a = Review()
        self.assertEqual(type(a.user_id), str)
        self.assertEqual(type(a.place_id), str)
        self.assertEqual(type(a.text), str)

    def test_attr_with_settr(self):
        c = Review()
        c.text = "Good"
        self.assertEqual(c.text, "Good")


if __name__ == "__main__":
    unittest.main()
