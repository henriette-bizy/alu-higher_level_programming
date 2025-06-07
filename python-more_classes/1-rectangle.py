#!/usr/bin/python3
<<<<<<< HEAD
"""A class Rectangle that defines a rectangle based on 0-rectangle.py"""


class Rectangle:
    """The Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle obj.
            height (int): The height of the rectangle obj.
=======
# 1-rectangle.py
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
        """property(get&set) for the width of the rectangle."""
=======
        """Get/set the width of the rectangle."""
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
        """property(get&set) for the height of the rectangle."""
=======
        """Get/set the height of the rectangle."""
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
