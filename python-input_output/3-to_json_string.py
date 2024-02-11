#!/usr/bin/python3
"""3. To JSON string"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)
    Args:
        my_obj: object to represent
    """
    return json.dumps(my_obj)
