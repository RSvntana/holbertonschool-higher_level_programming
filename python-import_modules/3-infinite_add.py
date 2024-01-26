#!/usr/bin/python3

import sys

if __name__ == "__main__":

    args = sys.argv[1:]

    num = []
    for i in args:
        num.append(int(i))

    total = sum(num)
    print(total, end="\n")
