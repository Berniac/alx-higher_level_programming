#!/usr/bin/python3
"""
Module that contains a function that reads
a text file and prints it to stdout
"""


def read_file(filename=""):
    """ Function that reads a text file(UTF-8) and
    prints it to stdout

    Args:
        filename: name of the file

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
