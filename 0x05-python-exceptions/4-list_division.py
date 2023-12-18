#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    n = []
    try:
        for i in range(list_length):
            j = my_list_1[i] / my_list_2[i]
            n.append(j)
    except ValueError:
        print("wrong type")
        n.append(0)
    except ZeroDivisionError:
        print("division by 0")
        n.append(0)
    except IndexError:
        print("out of range")
        n.append(0)
    finally:
        return n
