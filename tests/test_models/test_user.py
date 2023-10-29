#!/usr/bin/python3
"""
    Unittests for module models/user,py
"""
import unittest
from models.user import User
from models.base_model import BaseModel
import datetime
from time import sleep


class TestUserInstantiation(unittest.TestCase):
    """Test instantiation of User class"""
    def test_subclass_of(self):
        """Test if instance is subclass of BaseModel"""
        u = User()
        self.assertIsInstance(u, BaseModel)
        self.assertIsInstance(u, User)

    def test_no_arg(self):
        """Test without any argument"""
        u = User()
        self.assertIn("created_at", u.__dict__)
        self.assertIn("updated_at", u.__dict__)
        self.assertIn("id", u.__dict__)
        self.assertIsInstance(u.id, str)
        self.assertIsInstance(u.created_at, datetime.datetime)
        self.assertIsInstance(u.updated_at, datetime.datetime)

    def test_user_attr_with_default(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_set_attr(self):
        """Test for setting attr"""
        u = User()
        u.email = "airbnb@gmail.com"
        u.password = "clone"
        u.first_name = "unittest"
        u.last_name = "Airbnb"

        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))
        self.assertTrue(hasattr(u, "id"))

        self.assertTrue('email' in u.__dict__)
        self.assertTrue('id' in u.__dict__)
        self.assertTrue('created_at' in u.__dict__)
        self.assertTrue('updated_at' in u.__dict__)
        self.assertTrue('password' in u.__dict__)
        self.assertTrue('first_name' in u.__dict__)
        self.assertTrue('last_name' in u.__dict__)

        self.assertEqual(type(u.email), str)
        self.assertEqual(type(u.password), str)
        self.assertEqual(type(u.first_name), str)
        self.assertEqual(type(u.last_name), str)

    def test_save_method(self):
        """Test inherited save method"""
        u = User()
        t1 = u.updated_at
        u.save()
        t2 = u.updated_at
        self.assertNotEqual(t1, t2)

    def test_to_dict(self):
        """Test inherited to_dict method"""
        u = User()
        self.assertEqual('to_dict' in dir(u), True)

    def test_doc_string(self):
        """Test class docstring"""
        self.assertIsNotNone(User.__doc__)

    def test_class_attribute(self):
        """Test class attributes"""
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))


if __name__ == "__main__":
    unittest.main()
