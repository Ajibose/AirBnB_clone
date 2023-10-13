#!/usr/bin/env python3
"""
    Test suite for class 'BaseModel' of module `models/base_model'
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModelInstantiation(unittest.TestCase):
    """Test BaseModel instantiation"""
    def test_no_arg(self):
        b = BaseModel()
        self.assertTrue(b.id)

