#!/usr/bin/python3
"""Module for Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize a Square instance.
        Args:
            size (int): The size of the square."""
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """Calculate the area of the square.
        Returns:
            int: The area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
