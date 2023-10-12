#!/usr/bin/env python3
"""
    Contains storage class
"""


import json
import os


class FileStorage:
    """Serializes and deserializes to JSON file

    Attributes:
        file (str): Hold the path to JSON file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return dictionary object of all object
        """
        return self.__objects

    def new(self, obj):
        """Sets object"""

        k = f"{obj.__class__.__name__}.{obj.id}"
        type(self).__objects[k] = obj

    def save(self):
        """serializes obj to path"""
        my_dict = {}

        for k, v in self.__objects.items():
            v = v.to_dict()
            my_dict[k] = v

        with open(type(self).__file_path, mode="w", encoding="utf-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes obj from path"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        my_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }

        if os.path.exists(type(self).__file_path):
            with open(type(self).__file_path, "r", encoding="utf-8") as f:
                obj = json.load(f)
                for k in obj:
                    cls = k.split(".")[0]
                    self.__objects[k] = my_dict[cls](**obj[k])
