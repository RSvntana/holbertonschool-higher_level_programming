#!/usr/bin/python3
"""1. Write to a file"""


def write_file(filename="", text=""):
    """ writes as string to a text file
    Args:
        filename: name of the file
        text: text to write
        """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
