#!/usr/bin/env python3
"""
    Test suite for class 'BaseModel' of module `models/base_model'
"""
import unittest
from models.base_model import BaseModel
import datetime
import uuid


class TestBaseModelInstantiation(unittest.TestCase):
    """Test BaseModel instantiation"""
    def test_no_arg(self):
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))

    def test_multiple_instaces(self):
        """Test equality of the ids BaseModel instances"""
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()

        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.id, b3.id)
        self.assertNotEqual(b3.id, b2.id)

    def test_pos_arg(self):
        """Test the instantiation positional argument"""
        b = BaseModel(2)
        b1 = BaseModel(2, 3)
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "created_at"))

    def test_keyword_arg(self):
        """Test the instantiation keyword argument"""
        b = BaseModel(id=2)
        self.assertTrue(hasattr(b, "id"))
        self.assertEqual(b.id, 2)
        self.assertFalse(hasattr(b, "updated_at"))
        self.assertFalse(hasattr(b, "created_at"))

        b = BaseModel(id=2, created_at="2023-10-13T18:33:54.505580")
        self.assertTrue(hasattr(b, "id"))
        self.assertEqual(b.id, 2)
        self.assertTrue(hasattr(b, "created_at"))
        self.assertFalse(hasattr(b, "updated_at"))

        b = BaseModel(id=2, created_at="2023-10-13T18:33:54.505580", updated_at="2023-10-13T18:33:54.505580")
        self.assertTrue(hasattr(b, "id"))
        self.assertEqual(b.id, 2)
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))
        
        b = BaseModel(id=2, created_at="2023-10-13T18:33:54.505580", updated_at="2023-10-13T18:33:54.505580", name="Airbnb")
        self.assertTrue(hasattr(b, "id"))
        self.assertEqual(b.id, 2)
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at")) 
        self.assertTrue(hasattr(b, "name"))
        self.assertEqual(b.name, "Airbnb")

        b = BaseModel(first_name="unittest", last_name="Airbnb")
        self.assertFalse(hasattr(b, "updated_at"))
        self.assertFalse(hasattr(b, "created_at"))
        self.assertFalse(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "first_name"))
        self.assertEqual(b.first_name, "unittest")
        self.assertTrue(hasattr(b, "last_name"))
        self.assertEqual(b.last_name, "Airbnb")

        b = BaseModel(first_name=("unittest, Airbnb"))
        self.assertTrue(hasattr(b, "first_name"))
        self.assertEqual(b.first_name, ("unittest, Airbnb"))

        b = BaseModel(first_name=["unittest, Airbnb"])
        self.assertTrue(hasattr(b, "first_name"))
        self.assertEqual(b.first_name, ["unittest, Airbnb"])

    def test_none_arg(self):
        b = BaseModel(None)
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "id"))

        b = BaseModel(name=None)
        self.assertFalse(hasattr(b, "updated_at"))
        self.assertFalse(hasattr(b, "created_at"))
        self.assertFalse(hasattr(b, "id"))

    def test_inf_arg(self):
        b= BaseModel(float('inf'))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "id"))

        b = BaseModel(name=float('inf'))
        self.assertFalse(hasattr(b, "updated_at"))
        self.assertFalse(hasattr(b, "created_at"))
        self.assertFalse(hasattr(b, "id"))

    def test_nan_arg(self):
        b= BaseModel(float('nan'))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "id"))

        b = BaseModel(name=float('nan'))
        self.assertFalse(hasattr(b, "updated_at"))
        self.assertFalse(hasattr(b, "created_at"))
        self.assertFalse(hasattr(b, "id"))

    def test_setattr(self):
        b = BaseModel()
        b.name = "Airbnb"
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "name"))


class TestBaseModelStrMethod(unittest.TestCase):
    """Tests the str method of BaseModel"""
    def test_no_arg(self):
        """Test with no argument"""
        b = BaseModel()
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

    def test_pos_arg(self):
        """Test str method with positional arguments"""
        b = BaseModel(2)
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

        b = BaseModel(None)
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

        b = BaseModel(float('nan'))
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

        b = BaseModel(float('inf'))
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

    def test_keyword_arg(self):
        """Test str method with keyword instantiation"""
        b = BaseModel(name="Airbnb")
        with self.assertRaises(AttributeError):
            self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

        b = BaseModel(id="2")
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

        b = BaseModel(id=2)
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")

        b = BaseModel(id=[1, 2])
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}") 

        b = BaseModel(id=(1, 2))
        self.assertEqual(str(b), f"[BaseModel] ({b.id}) {b.__dict__}")


    def test_using_str(self):
        """Test str method using __str__"""
        b = BaseModel()
        self.assertEqual(b.__str__(), f"[BaseModel] ({b.id}) {b.__dict__}")

        b = BaseModel()
        # Test __str__ with arguments
        with self.assertRaises(TypeError):
            self.assertEqual(b.__str__(23), f"[BaseModel] ({b.id}) {b.__dict__}")

class TestBaseModelSave(unittest.TestCase):
    """Test the save method of BaseModel"""
    def test_no_arg(self):
        """Test with no arg"""
        b = BaseModel()
        t1 = b.updated_at

        b.save()

        t2 = b.updated_at
        self.assertNotEqual(t1, t2)

    def test_one_arg(self):
        """Test with one arg"""
        b = BaseModel()

        with self.assertRaises(TypeError):
            b.save("2023-13-12")

class TestBaseModelToDict(unittest.TestCase):
    """Test the to_dict method of BaseModel"""
    def test_no_arg(self):
        """Test with no arg"""
        b = BaseModel()
        my_dict = b.to_dict()

        self.assertIn("__class__", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)
        self.assertIn("id", my_dict)
        self.assertEqual(my_dict["__class__"], "BaseModel")
        self.assertIsInstance(my_dict["__class__"], str)
        self.assertIsInstance(my_dict["updated_at"], str)
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["id"], str)

        b = BaseModel(name="Airbnb")
        my_dict = b.to_dict()
        self.assertIn("__class__", my_dict)
        self.assertNotIn("created_at", my_dict)
        self.assertNotIn("updated_at", my_dict)
        self.assertNotIn("id", my_dict)
        self.assertIn("name", my_dict)
        self.assertEqual(my_dict["name"], "Airbnb")

        b = BaseModel(__class__="Airbnb")
        self.assertIn("__class__", my_dict)
        self.assertEqual(my_dict["__class__"], "BaseModel")

        b = BaseModel("Airbnb")
        my_dict = b.to_dict()

        self.assertIn("__class__", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)
        self.assertIn("id", my_dict)
        self.assertEqual(my_dict["__class__"], "BaseModel")
        self.assertIsInstance(my_dict["__class__"], str)
        self.assertIsInstance(my_dict["updated_at"], str)
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["id"], str)

    def test_with_arg(self):
        """Test to_dict with argument"""
        b = BaseModel()

        with self.assertRaises(TypeError):
            my_dict = b.to_dict(23)

    def test_after_setattr(self):
        """Test to_dict after setattr"""
        b = BaseModel()
        my_dict = b.to_dict()

        self.assertIn("__class__", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)
        self.assertIn("id", my_dict)
        self.assertNotIn("name", my_dict)

        b.name = "Airbnb"
        self.assertIn("__class__", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)
        self.assertIn("id", my_dict)
        self.assertNotIn("name", my_dict)

        my_dict = b.to_dict()
        self.assertIn("__class__", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)
        self.assertIn("id", my_dict)
        self.assertIn("name", my_dict)

    def test_from_dict_repr(self):
        """Test to_dict using another object dict repr"""
        b = BaseModel()
        b.name = "Airbnb"
        my_dict1 = b.to_dict()
        self.assertIn("name", my_dict1)

        b1 = BaseModel(**my_dict1)
        my_dict2 = b1.to_dict()
        self.assertIn("__class__", my_dict2)
        self.assertEqual(my_dict2["__class__"], "BaseModel")
        self.assertIn("name", my_dict2)
        self.assertEqual(my_dict2["name"], "Airbnb")

        self.assertCountEqual(my_dict1, my_dict2)
        self.assertEqual(my_dict1["created_at"], my_dict2["created_at"])
        self.assertEqual(my_dict1["updated_at"], my_dict2["updated_at"])
        self.assertDictEqual(my_dict1, my_dict2)




if __name__ == '__main__':
    unittest.main()
