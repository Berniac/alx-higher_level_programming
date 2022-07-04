#!/usr/bin/python3
"""
Module consisting of a function that checks if an object
is an instance of a class that inherited from a specified
class
"""


def inherits_from(obj, a_class):
    """ Function that returns true/false if object is/isn't an instance
    of a class that inherited from a_class

    Args:
        obj: object
        a_class: clas

    Returns:
        True if object is an instance of a class that inherited from a_class
        False otherwise
    """
    if type(obj) is a_class
        return False
    return isinstance(obj, a_class)
