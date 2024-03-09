#!usr/bin/env bash
"""This is a base class"""

import uuid
from datetime import datetime

class BaseModel:
    """This is a definition of base class"""
    def __init__(self, *args, **kwargs):
        """This is a constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns string representation"""
        class_name = self.__class__.__name__
        return f'[{class_name}] ({self.id} {self.__dict__})'

    def save(self):
        """Method to update updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
