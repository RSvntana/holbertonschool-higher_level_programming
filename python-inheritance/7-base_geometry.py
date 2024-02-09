#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """The BaseGeometry class."""

    def area(self):
        """Calculate area of the geometry.
        Raises:
            Exception: If area is not implemented.
        Args:
            self: the object itself.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value.
        Args:
            name (str): The name of the value.
            value (int): The value to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.name = name
        self.value = value
