#!/usr/bin/python3

def write_file(filename="", text=""):
    """Écrit une chaîne dans un fichier texte UTF-8 et retourne\
    le nombre de caractères écrits"""
    with open(filename, "w", encoding="utf-8") as f:
        characters_written = f.write(text)
    return characters_written
