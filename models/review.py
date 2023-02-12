#!/usr/bin/python3
"""description of class Review which inherits from BasedModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review
    Attributes:
        place_id (str) - refers to the Place.id
        user_id (str) - refers to the User.id
        text (str) - The contents of the review
    """
    place_id = ""
    user_id = ""
    text = ""
