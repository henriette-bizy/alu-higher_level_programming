#!/usr/bin/python3
<<<<<<< HEAD
"""A class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """property(get&set) for the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(val, int) for val in value) and
                all(val >= 0 for val in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Return the current area of the square."""
        return (self.__size**2)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for val in range(self.__position[0])]
            [print("#", end="") for val in range(self.__size)]
            print()
=======
"""Square class to represent a square"""


class Square:
    """
    Defines a Square and its basic properties
    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """

    def __init__(self, size=0, position=(0, 0)) -> None:
        """
        Innitialize the size of the square. the size can be specified.
        If they are not, the size defaults to 0
        :param size: int size of square ( > 0)
        :param: tuple (x, y) representing position
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.position = position
        self.size = size

    @property
    def size(self) -> int:
        """
        Retrieve the instance attribute size
        :return: the size of the square
        """
        return self.__size

    @property
    def position(self) -> tuple:
        """
        Retrieve the instance attribute position
        :return: the position (x, y)
        """
        return self.__position

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

    @position.setter
    def position(self, value: tuple) -> None:
        """
        Set the position
        :param: (x, y)
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
