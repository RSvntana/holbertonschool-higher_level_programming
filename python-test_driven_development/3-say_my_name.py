#!/usr/bin/python3
"""
This module will have a function
the prints the sentece
(My name is [first_name] [last_name])
"""


def say_my_name(first_name, last_name=""):
    """
        Function that check that first_name is a str,
        as well as last_name. If both are str it will
        print the sentece
        (My name is [first_name] [last_name])
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
