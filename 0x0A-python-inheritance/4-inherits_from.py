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
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
