#!/usr/bin/python3
<<<<<<< HEAD
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
=======
''' module: 4-inherits_from
'''


def inherits_from(obj, a_class):
    '''the object is an instance of a class inherited (directly or indirectly)
    obj: an object
    a_class: a class
    returns None
    '''
    return type(obj) != a_class and isinstance(obj, a_class)
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
