#!/usr/bin/python3
<<<<<<< HEAD
"""Define a class Square."""


class Square:
    """A class that defines a square"""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
=======
""" Square class to represent a sqaure"""


class Square:
    """ Define a square and its basic properties
    >>> sqaure_1 = Square()
    >>> sqaure_2 = Sqaure(87)
    """

    def __init__(self, size: int) -> None:
        """ __init__ the size with a params of int """
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        self.__size = size
