#!/usr/bin/python3
"""
Module that contains function that checks if an instance
is of a specified class
"""


def is_same_class(obj, a_class):
    """Function that returns True if the object is exactly an
    instance of specified class; otherwise False

    Args:
        obj: object
        a_class: class

    Returns:
        True if type of obj is a_class
        False otherwise
    """

    return type(obj) is a_class
