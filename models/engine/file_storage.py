#!/usr/bin/python3
"""Serializes instances to a JSON file and
deserializes JSON files to instances"""

import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """File storage class that serializes and deserializes to and from JSON"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Instantiation method"""
        pass

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets object into __objects with ID key pairing."""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to JSON file"""
        ndict = {}
        for key, value in FileStorage.__objects.items():
            ndict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(ndict, file)

    def reload(self):
        """Deserializes from JSON file"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                temp = json.load(file)
                for key, value in temp.items():
                    class_name = value["__class__"]
                    class_name = class_name.replace("models.", "")
                    gclass = eval(class_name)
                    self.__objects[key] = gclass(**value)
