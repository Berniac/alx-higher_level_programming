#!/usr/bin/python3
"""
Module that consists of class Square
that inherits from class Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that defines a square and inherits from rectangle class """
    def __init__(self, size):
        """ Method that initializes a Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method that returns a string with the area """
        return super().area()
