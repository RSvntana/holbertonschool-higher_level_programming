#!/usr/bin/python3
"""Module for Square class."""


class Square:
    """A class with a size attribute."""

    def __init__(self, size=0):
        """Initializes a Square object."""
        if not isinstance(size, int):  # isinstance() checks if size is an int
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
