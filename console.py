#!usr/bin/env bash
"""This is a command line"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """This is a class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Does nothing"""
        pass
    
    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
            return
        if class_name == "BaseModel":
            new_instance = BaseModel()
        else:
            new_instance = User()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])
    
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if not args:
            print([str(obj) for obj in storage.all().values()])
        else:
            class_name = args[0]
            if class_name not in {"BaseModel", "User"}:
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in storage.all().items()
                if key.startswith(class_name + ".")])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
