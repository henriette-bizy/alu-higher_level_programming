#!/usr/bin/python3
<<<<<<< HEAD
"""A class Rectangle that defines a rectangle based on 1-rectangle.py"""


class Rectangle:
    """The Rectangle class

    Attributes:
        number_of_instances (int): The number of Rectangle obj.
=======
# 9-rectangle.py
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
<<<<<<< HEAD
        """Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property(get&set) for the width of the Rectangle."""
=======
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
<<<<<<< HEAD
        """property(get&set) for the height of the Rectangle."""
=======
        """Get/set the height of the Rectangle."""
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
<<<<<<< HEAD
        """Returns the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
=======
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
<<<<<<< HEAD
        """Returns the Rectangle obj with a bigger area.

=======
        """Return the Rectangle with the greater area.
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
<<<<<<< HEAD
            return rect_1
        return rect_2
=======
            return (rect_1)
        return (rect_2)
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.
<<<<<<< HEAD

=======
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
<<<<<<< HEAD
        """Returns the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        outp = []
        for x in range(self.__height):
            [outp.append(str(self.print_symbol)) for y in range(self.__width)]
            if x != self.__height - 1:
                outp.append('\n')
        return "".join(outp)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        string = f"Rectangle({str(self.__width)}, {str(self.__height)})"
        return string

    def __del__(self):
        """Prints Bye rectangle... when a Rectangle obj is deleted"""
        Rectangle.number_of_instances -= 1
=======
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        print("Bye rectangle...")
