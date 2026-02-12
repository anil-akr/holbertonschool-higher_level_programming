#!/usr/bin/python3
"""Module 11-student
Defines a Student class with serialization/deserialization
"""

class Student:
    """Represents a student with first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance

        If attrs is a list of strings, only attributes in this list are included.
        Otherwise, all attributes are included.

        Args:
            attrs (list, optional): list of attribute names to retrieve

        Returns:
            dict: dictionary representation of the Student instance
        """
        if attrs is None:
            return self.__dict__.copy()
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance

        Args:
            json (dict): dictionary with keys matching public attribute names
        """
        for key, value in json.items():
            setattr(self, key, value)
