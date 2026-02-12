#!/usr/bin/python3
"""
task_01_pickle
Serialize and deserialize custom Python objects using pickle
"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.
        Returns True on success, None on failure.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            return True
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a file to create an instance of CustomObject.
        Returns the object on success, None on failure.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except (OSError, pickle.PickleError, EOFError):
            return None
