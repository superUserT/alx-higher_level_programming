#!/usr/bin/python3
"""A function that returns a copy of a list"""


def copy_list(l):
    if isinstance(l, list):
        return l[:]
