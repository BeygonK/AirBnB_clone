#!usr/bin/env bash
"""This is a tests module"""

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """This class inherits from unittest"""

    def test_instance_creation(self):
        """Test instance"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attributes_assignment(self):
        """Test attribute assignment"""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_to_dict_method(self):
        """Test to dict method"""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        user_dict = user.to_dict()
        expected_dict = {
            "email": "test@example.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
            "__class__": "User",
            "id": user.id,
            "created_at": user.created_at.isoformat(),
            "updated_at": user.updated_at.isoformat()
        }
        self.assertDictEqual(user_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()
