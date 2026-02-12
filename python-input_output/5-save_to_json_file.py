#!/usr/bin/python3
"""Module that defines a function to save a Python object to
a file in JSON format."""

import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object to a file as JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
        f.write("\n")
