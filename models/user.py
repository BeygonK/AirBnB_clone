#!usr/bin/env bash
"""This is a module for the user"""


from models.base_model import BaseModel

class User(BaseModel):
    """This is a class definition"""

    def __init__(self, *args, **kwargs):
        """Initializes User instance"""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")
