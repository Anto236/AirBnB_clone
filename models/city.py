#!/usr/bin/python3
"""class City which inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """defines class City
    Attributes:
        state_id (str) - dtate.id
        name (str) - name of str
    """
    state_id = ""
    name = ""
