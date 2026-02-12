#!/usr/bin/python3
"""Module that defines a function to convert a class instance
to a dictionary for JSON serialization.
"""


def class_to_json(obj):
    """Return the dictionary representation of a class instance attributes.

    Args:
        obj (object): The class instance.

    Returns:
        dict: Dictionary of the instance's attributes.
    """
    return obj.__dict__
