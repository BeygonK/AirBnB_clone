#!/usr/bin/python3
"""This is a class module"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """This is class definition"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary"""
        return self.__objects

    def new(self, obj):
        """creates new object for storage"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes objects to JSON file"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Loads from json"""
        my_classes = {
                'BaseModel': BaseModel,
                'User': User,
                'Place': Place,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Review': Review
                }
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_ = my_classes[class_name]
                    obj = class_(**value)  # Create a User instance
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

