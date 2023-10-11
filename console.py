#!/usr/bin/env python3
"""
    Contains the Console class for the project
"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """The command interpreter

    Attributes:
        prompt(str): The prompt to use for the interpreter
    """
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
        all_class = {
                "BaseModel": BaseModel
                }

        if not cls_name:
            print("** class name missing **")
            return

        if cls_name not in all_class:
            print("** class doesn't exist **")
            return

        obj = all_class[cls_name]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Print the string representation of an istance"""
        all_class = {
                "BaseModel": BaseModel
                }
        arg_list = arg.split(" ")
        cls_name = arg_list[0]
        if not cls_name:
            print("** class name missing **")
            return

        if cls_name not in all_class:
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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
