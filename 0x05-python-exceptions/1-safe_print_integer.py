#!/usr/bin/python2
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return ture
    except (TypeError, ValueError):
        return false
