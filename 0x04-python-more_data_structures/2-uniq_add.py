#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = set()
    sum = 0
    for item in my_list:
        if item not in seen:
            seen.add(item)
            sum += item
    return sum
