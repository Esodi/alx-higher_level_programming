#!/usr/bin/python3
def uppercase(str):
    c = []
    for char in str:
        if (ord(char) >= 97) and (ord(char) < 123):
            x = ord(char) - 32
            c.append(chr(x))
            #print("{}".format(chr(x)), end="")
        else:
            #print("{}".format(char), end="")
            c.append(char)
    h = ''.join(c)
    print(h)
