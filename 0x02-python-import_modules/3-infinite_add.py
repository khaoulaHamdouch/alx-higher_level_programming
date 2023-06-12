#!/usr/bin/python3
if __name__ = "__main__":
    """Prints the addition of all arguments."""
    import sys
    arg_num = len(argv) - 1
    if arg_num == 0:
        print("{}".format(arg_num))
    else:
        total = []
        for i in range(1, arg_num + 1):
            total.append(int(argv[i]))
        print("{}".format(total))
