#!/usr/bin/python3
"""Importing storage variable"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
