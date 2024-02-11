#!/usr/bin/python3
"""9-student.py."""


class Student:
    """Studetn class"""

    def __init__(self, first_name, last_name, age):
        """__init__
        Args:
            firt_name (str): first name
            last_name (str): last name
            age (int): age
            """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json"""
        return self.__dict__
