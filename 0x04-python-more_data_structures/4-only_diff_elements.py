#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    s1 = list(set_1)
    s2 = list(set_2)
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                del s1[i]
                del s2[j]
    k = s1 + s2
    return k
