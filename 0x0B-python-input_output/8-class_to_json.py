#!/usr/bin/python3
"""
Module that contains function that returns the dictionary description
with simple data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """ Function thta returns the dictionary description with simple
    data structure for JSON serialization of an object
    """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
