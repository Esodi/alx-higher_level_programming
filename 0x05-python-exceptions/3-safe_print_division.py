#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        print('Inside result: None')
    finally:
        if b / a != 0:
            print("Inside result: {:.1f}".format(c))
            return c
        else:
            return None
