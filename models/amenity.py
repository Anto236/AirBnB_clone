#!/usr/bin/python3
"""class Amenity which inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """defines class Amenity
    Attributes:
        name (str) - name of the amenity
    """
    name = ""
