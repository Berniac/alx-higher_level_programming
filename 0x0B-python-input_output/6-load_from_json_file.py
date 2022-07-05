#!/usr/bin/python3
"""
Module that contains function that creates an Object
from a "JSON file"
"""
import json


def load_from_json_file(filename):
    """ Function that creates an Object from a JSON
    file

    Args:
        filename: name of the file

    """


    with open(filename. 'r', encoding="utf-8") as f:
        return json.load(f)
