#!/usr/bin/env bash
"""This is a class module"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
