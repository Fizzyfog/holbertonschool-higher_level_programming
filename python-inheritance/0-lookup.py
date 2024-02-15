#!/usr/bin/python3
""" Module for object attribute lookup function."""


def lookup(obj: object) -> list:
    """ Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object for which to list the attributes and methods.

    Returns:
        list: A list of strings representing the attributes and methods of the object.
    """

    return dir(obj)
