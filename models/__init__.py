#!usr/bin/env bash
"""This is a iniit module"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
