#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization method for the Square class.
        
        Args:
            size (int): Size of the square.
            x (int): x position of the square.
            y (int): y position of the square.
            id (int): id of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size, updates both width and height."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update method for the Square class.
        
        Args:
            args (list): List of arguments.
            kwargs (dict): Dictionary of arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of the Square."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
