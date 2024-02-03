#!/usr/bin/python3
""" prints a text with 2 new lines after each of these characters: ., ?and:"""


def text_indentation(text):
    """
    >>> text_indentation("")
    <BLANKLINE>

    >>> text_indentation('')
    <BLANKLINE>

    >>> text_indentation("?")
    <BLANKLINE>

    >>> text_indentation(":")
    <BLANKLINE>

    >>> text_indentation(".")
    <BLANKLINE>

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    space = False  # flag to check if there is a space
    for char in text:
        if not space:
            if char == ' ':
                continue
            else:
                space = True
        if char == '.' or char == '?' or char == ':':
            print(char)
            print()
            space = False
        else:
            print(char, end="")
