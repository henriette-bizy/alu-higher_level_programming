#!/usr/bin/python3
<<<<<<< HEAD
"""This module define classes for singly-linked list impementation"""


class Node:
    """Objs of this clsass represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

=======

"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data: int, next_node=None):
        """Initialize a new Node.
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
<<<<<<< HEAD
        """property(get&set) for the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if (not isinstance(value, int)):
=======
        """Get the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
<<<<<<< HEAD
        """property(get&set) for the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (not isinstance(value, Node) and value is not None):
=======
        """Get the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
<<<<<<< HEAD
    """This class represents a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
=======
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
<<<<<<< HEAD

        The node is inserted into the list at the sorted
        position in the list (increasing order)

        Args:
            value (Node): The new Node to insert.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (current_node.next_node is not None and
                    current_node.next_node.data < value):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        """The print() representation of a SinglyLinkedList obj"""
        node_list = []
        current_node = self.__head
        while (current_node is not None):
            node_list.append(str(current_node.data))
            current_node = current_node.next_node
        return '\n'.join(node_list)
=======
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
>>>>>>> 7f1687829a3748d861ca00bc849ca9324470e555
