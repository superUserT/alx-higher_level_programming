#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format())
    except (IndexError, ValueError):
        return False
    return True
        