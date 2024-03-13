#!/usr/bin/python3
"""This is a iniit module"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
