#!/usr/bin/python3
"""
Module that consists of a class that inherits from
another class list and a method that prints the
list sorted in ascending order
"""


class MyList(list):
    """ Class that inherits from class list

    Args:
        list: class list

    """

    def print_sorted(self):
        """ Method that prints the list sorted in ascending order"""
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
