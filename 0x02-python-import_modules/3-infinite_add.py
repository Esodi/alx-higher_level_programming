#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    l = len(args)
    ans = 0
    for i in range(1, (l + 1)):
        ans = ans + int(sys.argv[i])
    print("{}".format(ans))
