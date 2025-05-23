#!/usr/bin/python3
"""Define a class Square."""


class Square:
<<<<<<< HEAD
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

=======
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
<<<<<<< HEAD
        """property(get&set) for the current size of the square."""
=======
        """Get/set the current size of the square."""
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
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
<<<<<<< HEAD
        """property(get&set) for the current position of the square."""
=======
        """Get/set the current position of the square."""
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
<<<<<<< HEAD
        """Prints in stdout the square with the character #."""
=======
        """Print the square with the # character."""
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
<<<<<<< HEAD
            [print(" ", end="") for x in range(self.__position[0])]
            [print("#", end="") for y in range(self.__size)]
            print()

    def __str__(self):
        """The print() representation for a Square obj."""
        if self.__size != 0:
            [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            if i != self.__size - 1:
                print()
=======
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        return ("")
