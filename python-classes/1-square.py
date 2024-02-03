#!/usr/bin/python3
"""Square module - provides an empty class Square"""


class Square:
    """This is a Square class.

    This class doesn't have any attributes or methods yet, but it can be used
    as a starting point for creating a Square object.

    """

    def __init__(self, size):
        """Initializes a Square with a given size

        Args:
            size (int): size of the square

        """
        self.__size = size  # this is a private attribute
