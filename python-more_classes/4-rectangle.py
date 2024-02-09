#!/usr/bin/python3
"""
This is a docstring for the Rectangle class.
"""

class Rectangle:
    """
    This is a docstring for the Rectangle class.
    """
    def __init__(self, width=0, height=0):
        """
        This adding the need atributtes
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This is a docstring for the width method.
        this returns self.__width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        This is a docstring for the width setter method.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        This is a docstring for the height method.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This is a docstring for the height setter method.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Area """
        return self.__width * self.__height

    def perimeter(self):
        """ Perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append("#")for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """ Represtion """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) +  ")"
        return rect