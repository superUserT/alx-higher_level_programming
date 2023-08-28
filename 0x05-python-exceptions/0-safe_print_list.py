#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    while 0 < x < 4: 
        try: 
            for i in range(x):
                print(my_list[i], end=" ")
                return x
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            return len(my_list)

