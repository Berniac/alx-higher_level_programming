#!/usr/bin/python3
"""
Module that contains function that adds a new attribute
to an object
"""


def add_attribute(obj, name, value):
    """ Function that adds a new attribute to an object

    Args:
        obj: object
        name: attribute name
        value: attribute value

    Raises:
        TypeError: when attribute can't be added

    """

    if not hasattr(obj, "__dict__"):
        raise TypeError('can\'t add new attribute')
    else:
        setattr(obj, name, value)
