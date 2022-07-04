#!/usr/bin/python3
"""
Module that consists of a functiion that returns list of
attributes and methods of obj

"""


def lookup(obj):
    """
    return the list of what is inside the obj
    """
    return dir(obj)
