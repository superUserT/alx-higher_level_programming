#!/usr/bin/python3
""" module finds the peak of a number """ 


def find_peak(list_of_integers):
    """
        find the peak of list of numbers

        Args:
            list_of_integers: list of integers

        Returns: the number of the peak
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
