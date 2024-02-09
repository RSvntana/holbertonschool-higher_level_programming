#!/usr/bin/python3
"""Module that checks if an object is an instance of a class
or an instance of a class that inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class
    checks if an object is an instance of a class
    Arg:
        obj: the object
        a_class: the class
    Return: True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
