#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a function to check if an obj is an instance of a given class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specific class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) is a_class:
=======
# 2-is_same_class.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        return True
    return False
