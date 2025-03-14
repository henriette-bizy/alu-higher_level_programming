#!/usr/bin/python3
<<<<<<< HEAD
"""Creates a Mylist class that inherits from list."""


class MyList(list):
    """Mylist class => A sub class of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
=======
''' Module: 1-my_list
'''


class MyList(list):
    ''' Represents a MyList
    '''

    def print_sorted(self):
        '''
        prints the list, but sorted
        '''
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        print(sorted(self))
