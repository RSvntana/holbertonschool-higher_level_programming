#!/usr/bin/python3
"""
This is a docstring for the Rectangle class.
"""

class Rectangle:
    
    
    """
    This is a docstring for the Rectangle class.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        This adding the need attributes
        """
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the areas of two rectangles and returns
        the rectangle with the larger area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the larger area.

        Raises:
            TypeError: If either rect_1 or rect_2 is't
            an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a square Rectangle object with the given size.

        Args:
            size (int): The size of the square.

        Returns:
            Rectangle: A Rectangle object representing a square
            with equal with and height.
        """
        return Rectangle(width=size, height=size)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """ Representation """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
