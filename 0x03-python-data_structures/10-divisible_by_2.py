#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_lite = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            list_lite.append(True)
        else:
            list_lite.append(False)
    return list_lite
