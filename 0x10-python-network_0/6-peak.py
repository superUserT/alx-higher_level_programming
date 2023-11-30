#!/usr/bin/python3
# finding the peak within a list 


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    peak_list = []

    if len(list_of_integers) == 0:
        return None
    else:
        peak_list.append(max(list_of_integers))

    string_converted_list = ' '.join(map(str, peak_list))

    return string_converted_list
