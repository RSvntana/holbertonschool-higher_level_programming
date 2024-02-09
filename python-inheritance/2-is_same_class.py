#!/usr/bin/python3
"""Module that checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """is_same_class
    checks if an object is an instance of a class
    Arg:
        obj: the object
        a_class: the class
    Return: True or False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
