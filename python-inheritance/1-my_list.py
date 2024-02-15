#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.
The class includes a method to print a sorted version of the list.
"""


class MyList(list):
    """
    A class that inherits from list with an additional method
      to print the list sorted.

    Args:
        list (list): The list to be sorted and printed.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        """
        print(sorted(self))
