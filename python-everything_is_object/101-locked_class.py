#!/usr/bin/python3
<<<<<<< HEAD
"""This module defines a class `LockedClass`."""
=======
"""Defines a locked class."""
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555


class LockedClass:
    """
<<<<<<< HEAD
    prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name
=======
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
    """

    __slots__ = ["first_name"]
