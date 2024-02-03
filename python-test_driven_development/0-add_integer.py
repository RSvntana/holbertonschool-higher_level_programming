#!/usr/bin/python3
"""add_integer - function
Attribute:
    a: first integer
    b: second integer
return: sum of a and b"""


def add_integer(a, b=98):
    """Returns sum of a and b
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer("School", -30)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer()
    Traceback (most recent call last):
        ...
    TypeError: add_integer() missing 1 required positional argument: 'a' """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
