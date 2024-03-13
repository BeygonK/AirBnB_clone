#!/usr/bin/python3
"""This is a module for the user"""


from models.base_model import BaseModel

class User(BaseModel):
    """This is a class definition"""
    email=""
    password=""
    first_name=""
    last_name=""
