#!/usr/bin/python3
"""Module that defines a function to convert a class instance to a dictionary for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary representation of a class instance attributes."""
    return obj.__dict__
