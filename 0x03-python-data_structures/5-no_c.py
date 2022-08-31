#!/usr/bin/python3
def no_c(my_string):
    copystr = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            copystr += x
    return copystr
