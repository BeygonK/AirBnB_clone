#!usr/bin/env bash
"""This is a test module"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """This is a definition of a class"""
    def setUp(self):
        self.base_model = BaseModel()

    def test_save(self):
        """Tests save method"""
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_to_dict(self):
        """Test dict method"""
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

        # Check if created_at and updated_at are strings
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)



if __name__ == '__main__':
    unittest.main()
