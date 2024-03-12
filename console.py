#!usr/bin/env bash
"""This is a command line"""

import cmd

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
