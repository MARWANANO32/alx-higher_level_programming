#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    op = 0
    ou = 0
    while op < x:
        try:
            print("{:d}".format(my_list[op]), end = '')
            ou += 1
        except (ValueError, TypeError):
            pass
        op += 1
    print()
    return (ou)

