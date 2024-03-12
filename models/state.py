#!/usr/bin/env bash
"""This is module for State"""

from models.base_mode import BaseModel

class State(BaseModel):
    """State class inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
