#!/usr/bin/python3
<<<<<<< HEAD
"""A class Rectangle that defines a rectangle based on 1-rectangle.py"""


class Rectangle:
    """The Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
=======
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        """
        self.width = width
        self.height = height

    @property
    def width(self):
<<<<<<< HEAD
        """property(get&set) for the width of the Rectangle."""
=======
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

    def __str__(self):
<<<<<<< HEAD
        """Returns the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        output = []
        for x in range(self.__height):
            [output.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                output.append('\n')
        return "".join(output)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        string = f"Rectangle({str(self.__width)}, {str(self.__height)})"
        return string
=======
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
