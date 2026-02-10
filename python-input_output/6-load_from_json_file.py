#!/usr/bin/python3

import json


def load_from_json_file(filename):
    """Lit un fichier JSON et retourne l'objet Python correspondant"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
