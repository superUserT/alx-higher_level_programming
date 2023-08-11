#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    arguments = argv[1:]
    argc = len(arguments)
    if (argc == 0):
        print("0 arguments.")
    elif (argc == 1):
        print("1 argument:")
    else:
        print(f"{argc} arguments:")
    for items in range(argc):
        print(f"{items + 1}: {argc[items]}")
