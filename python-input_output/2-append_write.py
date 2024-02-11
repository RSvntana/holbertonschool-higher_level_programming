#!/usr/bin/python3
"""2. Append to a file"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file
    Args:
        filename: name of the file
        text: text to append
    """
    with open(filename, 'a') as f:
        return f.write(text)
