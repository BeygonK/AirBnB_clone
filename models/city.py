#!/usr/bin/env bash
"""This is module for city"""

from models.base_mode import BaseModel

class City(BaseModel):
    """City class inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', "")
        self.name = kwargs.get('name', "")
