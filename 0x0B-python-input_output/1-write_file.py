#!/usr/bin/python3
"""
Module that contains function that writes a
string to a text file and returns the number
of characters written.
"""


def write_file(filename="", text=""):
    """ Function that write a string to a text file and
    returns the number of characters written

    Args:
        filename: name of file
        text: string

    """

    with open(filename, 'w', encoding="utf-8") as f:
       return f.write(text)
