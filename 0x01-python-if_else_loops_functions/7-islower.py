#!/usr/bin/python3
def islower(c):
    if (c == '') or (c == '7'):
        return
    for i in range(33, 123):
        if (i >= 97) and (i < 123):
            if (chr(i) == c):
                return True
        elif (i >= 65) and (i < 91):
            if (chr(i) == c):
                return False
        else:
            continue
