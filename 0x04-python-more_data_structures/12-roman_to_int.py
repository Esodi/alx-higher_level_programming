#!/usr/bin/python3
def roman_to_int(roman_string):
    d = {1000 : 'M', 500 : 'D', 100 : 'C', 50 : 'L', 10 : 'X', 5 : 'V', 1 : 'I'}
    if not roman_string:
        return 0
    s = 0
    for i in roman_string:
        for k in d:
            if i  == d[k]:
                s = s + k
    return s
