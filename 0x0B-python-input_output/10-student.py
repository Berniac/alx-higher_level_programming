#!/usr/bin/python3
"""
Module that defines the Student class
"""


class Student:
    """ Class that creates student instances """

    def __init__(self, first_name, last_name, age):
        """ Special initialization method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        if type(attrs) is not list:
            return (self.__dict__)
        else:
            new = {}
            ob = self.__dict__
            for i in attrs:
                for ele in ob:
                    if (i == ele):
                        new[i] = ob[i]
            return (new)
