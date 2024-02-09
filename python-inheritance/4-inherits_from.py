#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class. Otherwise return False.
    Args:
        obj: object to check
        a_class: class to check against
    Retunrs:
        True if obj is instance of class that inherited from a_class
        False otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
