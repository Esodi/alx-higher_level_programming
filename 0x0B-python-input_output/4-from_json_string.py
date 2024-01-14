#!/usr/bin/python3
"""a module with from_json_string() function"""
import json


def from_json_string(my_str):
    '''a function that returns an object (Python data structure)'''

    return json.loads(my_str)
