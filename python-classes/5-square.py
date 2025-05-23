#!/usr/bin/python3
<<<<<<< HEAD
"""A class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """property(get&set) for the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size**2)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        for x in range(self.__size):
            [print("#", end="") for num in range(self.__size)]
            print()
        if self.__size == 0:
            print("")
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

        self.__size = size

    @property
    def size(self) -> int:
        """
        Retrieve the instance attribute size
        :return: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        """
        Set the value of the size
        :param: int size
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self) -> int:
        """
        Calculates and returns the area of the square
        :return: the area of the square
        """
        return self.__size ** 2

    def my_print(self) -> None:
        """
        Print to the stdout '#' * size
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
