#!/usr/bin/python3
"""function that return if instance is part of the class"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class.

    Args:
        obj (any): The object to check.
        a_class (any): The class to check against.

    Returns:
        bool: True if the object is an instance of the class,
        False otherwise.
    """
    return type(obj) is a_class
