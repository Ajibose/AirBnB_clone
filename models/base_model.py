#!/usr/bin/env python3
"""
    Contains the Base class for all other class in this Project
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """The base class"""
    def __init__(self, *args, **kwargs):
        """The instantiation method"""
        if kwargs:
            for k, v in kwargs.items():
                if (k == "__class__"):
                    continue
                if (k == "created_at"):
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if (k == "updated_at"):
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """The class string function"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at field"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns dictionary representation of the class instance"""
        my_dict = {}
        for k, v in self.__dict__.items():
            if (type(v) == datetime):
                v = v.isoformat()

            my_dict[k] = v
        my_dict["__class__"] = self.__class__.__name__

        return my_dict
