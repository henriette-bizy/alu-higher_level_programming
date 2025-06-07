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
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return (self.__size**2)
=======
"""Square class to represent a square"""


class Square:
    """
    Defines a Square and its basic properties
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

        self.__size = size

    def area(self) -> int:
        """
        Calculates and returns the area of the square
        :return: the area of the square
        """

        return self.__size ** 2
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
