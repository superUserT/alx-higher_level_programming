#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    ints = []
    if len(argv) < 2:
        print(int(argv[1]))
    for arg in argv[1:]:
        try:
            ints.append(int(arg))
        except ValueError:
            print(f"{arg} is not a valid number.")
    sum = 0
    for ints in ints:
        sum += ints
    print(sum)
