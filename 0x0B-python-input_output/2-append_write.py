#!/usr/bin/python3
"""
Module that contains function that appends a
string to a text file and returns the number
of characters written.
"""


def append_write(filename="", text=""):
    """ Function that appends a string to a text file
    and returns the number of characters written

    Args:
        filename: name of file
        text: string

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
