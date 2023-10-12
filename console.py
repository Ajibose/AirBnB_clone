#!/usr/bin/env python3
"""
    Contains the Console class for the project
"""
import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """The command interpreter

    Attributes:
        prompt(str): The prompt to use for the interpreter
    """
    all_class = {
            "BaseModel": BaseModel
            }
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help(self, arg):
        """Help command"""
        print("")

    def do_EOF(self, arg):
        """CTRL-D command to exit the interpreter"""
        print("")
        return True

    def emptyline(self, line):
        """continue on encounter with an empty line + ENTER"""
        pass

    def do_create(self, arg):
        """Create a new instance of models classes"""
        cls_name = arg.split(" ")[0]

        if not cls_name:
            print("** class name missing **")
            return

        if cls_name not in HBNBCommand.all_class:
            print("** class doesn't exist **")
            return

        obj = HBNBCommand.all_class[cls_name]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Print the string representation of an istance"""
        arg_list = arg.split(" ")
        cls_name = arg_list[0]
        if not cls_name:
            print("** class name missing **")
            return

        if cls_name not in HBNBCommand.all_class:
            print("** class doesn't exist **")
            return

        cls_id = arg_list[1]
        if not cls_id:
            print("** instance id missing **")
            return

        storage.reload()
        objs = storage.all()

        for k, v in objs.items():
            if k.split(".")[1] == cls_id:
                print(v)
                return

        print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        my_dict = {}
        arg_list = arg.split(" ")
        cls_name = arg_list[0]
        if not cls_name:
            print("** class name missing **")
            return

        if cls_name not in HBNBCommand.all_class:
            print("** class doesn't exist **")
            return

        cls_id = arg_list[1]
        if not cls_id:
            print("** instance id missing **")
            return

        storage.reload()
        objs = storage.all()

        key = "{}.{}".format(cls_name, cls_id)
        try:
            del objs[key]
            storage.save()

            with open("file.json", "w", encoding="utf-8") as f:
                json.dump(my_dict, f)
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
            based or not on the class name"""

        objs_list = []
        storage.reload()
        my_dict = storage.all()

        if len(arg) == 0:
            for v in my_dict.values():
                v = str(v)
                objs_list.append(v)
            
        else:
            arg_list = arg.split(" ")
            cls_name = arg_list[0]
            if cls_name not in HBNBCommand.all_class:
                print("** class doesn't exist **")
                return

            for k, v in my_dict.items():
                if k.split(".")[0] == cls_name:
                    v = str(v)
                    objs_list.append(v)

        print(json.dumps(objs_list))

    def do_update(self, arg):
        """Update or add an attribute to an instance"""

        arg_list = arg.split(" ")
        cls_name = arg_list[0]
        if not cls_name:
            print("** class name missing **")
            return

        if cls_name not in HBNBCommand.all_class:
            print("** class doesn't exist **")
            return

        cls_id = arg_list[1]
        if not cls_id:
            print("** instance id missing **")
            return

        attr_name = arg_list[2]
        if not attr_name:
            print("** attribute name missing **")
            return

        val = arg_list[3]
        if not val:
            print("** value missing **")
            return

        storage.reload()
        my_dict = storage.all()

        key = cls_name + "." + cls_id

        if key in my_dict:
            obj = my_dict[key]
            setattr(obj, attr_name, val.replace("\"", ""))
            storage.new(obj)
            storage.save()
        else:
            print("** no instance found **")






if __name__ == '__main__':
    HBNBCommand().cmdloop()
