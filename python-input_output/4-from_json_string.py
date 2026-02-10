#!/usr/bin/python3

import json


def from_json_string(my_str):
    """Retourne l'objet Python représenté par une chaîne JSON"""
    return json.loads(my_str)
