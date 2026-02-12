#!/usr/bin/python3
"""
task_00_basic_serialization
Module for basic JSON serialization and deserialization
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.
    If the file exists, it will be replaced.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it into a Python dictionary.
    Returns the dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
