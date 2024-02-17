#!/usr/bin/python3
""" Base class """
import json
import turtle


class Base:
    """Base class for managing id attribute and providing utility methods."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class.

        Args:
            id (int): ID of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation.
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects to a file in JSON format.

        Args:
            list_objs (list): List of objects to save.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes set from a dictionary.

        Args:
            dictionary (dict): Dictionary of attributes.

        Returns:
            Base: Instance of the class.
        """
        dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Loads objects from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_shapes):
        """Draws shapes using the turtle module.

        Args:
            list_shapes (list): List of shapes to draw.
        """
        turtle.speed(2)
        for shape in list_shapes:
            turtle.penup()
            turtle.goto(shape.x, shape.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(shape.size)
                turtle.left(90)
