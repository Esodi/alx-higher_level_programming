#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    par = sys.argv[1:]
    if (len(par) == 0):
        print("{} arguments.".format(len(par)))
    elif (len(par) == 1):
        print("{} argument:".format(len(par)))
        print("{}: {}".format(len(par), sys.argv[1]))
    else:
        print("{} arguments:".format(len(par)))
        for i in range(1, (len(par) + 1)):
            print("{}: {}".format(i, sys.argv[i]))
