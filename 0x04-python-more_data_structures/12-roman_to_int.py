#!/usr/bin/python3
def roman_to_int(roman_string):
    d = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    if not roman_string or not isinstance(roman_string, str):
        return 0
    s = []
    for i in roman_string:
        for k in d:
            if i == d[k]:
                s.append(k)
    n = 0
    c = 0
    for j in range(0, len(s)):
        if c < s[j]:
            s[j] = s[j] - c
            n = n - c
        n += s[j]
        c = s[j]
    return n
