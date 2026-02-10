def read_file(filename=""):
    """Lit un fichier texte UTF-8 et l'affiche sur la sortie standard"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
