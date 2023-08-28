#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        try: 
            for i in range(x):
                print(my_list[i], end=" ")
                return x
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            return len(my_list)

