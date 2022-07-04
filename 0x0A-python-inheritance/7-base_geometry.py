#!/usr/bin/python3
"""
Module that conssists of class BaseGeometry
"""


class BaseGeometry:
    """ Class that defines attributesof Geometric shapes """
    def area(self):
        """ Method that defines area of a geometric shape """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that receives the value property

        Args:
            name: name of object
            value: value of property

        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
