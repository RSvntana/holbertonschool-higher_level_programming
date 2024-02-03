#!/usr/bin/python3
"""Square class"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """Initializes Square Class"""
        self.__size = size

    @property
    def size(self):
        """Gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of square"""
        return self.__size ** 2
