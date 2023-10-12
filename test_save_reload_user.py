#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)


print("-- Create a new State --")
my_state = State()
my_state.name = "london"
my_state.save()
print(my_state)

print("-- Create a new city --")
my_city = City()
my_city.name = "london"
my_city.state_id = "london"
my_city.save()
print(my_city)