#!/usr/bin/python3
"""a module with save_to_json_file() function"""
import json


def save_to_json_file(my_obj, filename):
    '''a function that writes an Object to a text file'''

    with open(filename, mode='w', encoding='utf-8') as f:
        j = json.dumps(my_obj)
        f.write(j)
