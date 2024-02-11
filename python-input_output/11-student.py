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

    def to_json(self, attrs=None):
        """to_json
        Args:
            attrs (list): list of attributes
            Returns:
                dict: dictionary of attributes
        """
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        for i in json:
            self.__dict__[i] = json[i]
