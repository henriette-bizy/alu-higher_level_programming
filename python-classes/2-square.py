#!/usr/bin/python3
<<<<<<< HEAD
"""Define a class Square."""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
=======
"""Square class to represent a square"""


class Square:
    """
    Defines a Square and its basic properties
    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """

    def __init__(self, size=0) -> None:
        """
        Innitialize the size of the square. the size can be specified.
        If they are not, the size defaults to 0
        :param size: int size of square ( > 0)
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        self.__size = size
