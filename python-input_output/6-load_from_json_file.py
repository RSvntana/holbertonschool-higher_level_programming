#!/usr/bin/python3
"""6. Load from JSON file"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file
    Args:
        filename: file to read from
    """
    with open(filename, 'r') as f:
        return json.load(f)
