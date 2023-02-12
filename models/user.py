#!/usr/bin/python3
"""Holds User class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Public class attributes
    email - email address
    password - password
    first_name - first name
    last_name - last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
