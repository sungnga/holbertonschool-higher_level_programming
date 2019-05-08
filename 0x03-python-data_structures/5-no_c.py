#!/usr/bin/python3

def no_c(my_string):
    new_str = ''
    if my_string:
        for i in my_string:
            if i != 'C' and i != 'c':
                new_str += i
    return new_str
