#!/usr/bin/python3
"""5. Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
        my_obj: object to represent
        filename: file to write to
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
