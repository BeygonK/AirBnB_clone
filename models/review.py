#!/usr/bin/python3
"""This is a class module"""


from models.base_model import BaseModel

class Review(BaseModel):
    """Review class inherits from BaseModel"""
    place_id=""
    user_id=""
    text=""
