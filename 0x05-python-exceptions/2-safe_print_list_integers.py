#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    countVar = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            countVar += 1
    except (IndexError, ValueError):
        pass
    finally:
        print()
        return countVar
