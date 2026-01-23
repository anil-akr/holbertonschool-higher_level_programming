#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after each '.', '?', or ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', or ':'.

    Args:
        text (str): text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length:
        line = ""
        while i < length and text[i] not in ".?:":
            line += text[i]
            i += 1
        # add the punctuation if we stopped at it
        if i < length and text[i] in ".?:":
            line += text[i]
            i += 1
        # print line stripped of spaces + 2 newlines
        print(line.strip())
        print()
        # skip any spaces after punctuation
        while i < length and text[i] == " ":
            i += 1
