#!/usr/bin/python3/
"""
This module will have a function
that print a square based on the
variable size. Using # to shape
draw the shape.
"""


def print_square(size):
    """
        Function that print a square with '#'
        size - is the size lenght of the square
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(size):
        print("#" * size)
