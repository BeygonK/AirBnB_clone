#!usr/bin/env bash
"""This is a class module"""

import json

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
        from models.base_model import BaseModel
        from models.user import User  # Import the User class here
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'User':  # Check if the class name is User
                        obj = User(**value)  # Create a User instance
                    else:
                        class_ = eval(class_name)  # Convert string to class object
                        obj = class_(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

