#!/usr/bin/python3
"""Define a MagicClass that does exactly as the bytecode provided."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.
<<<<<<< HEAD

=======
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
