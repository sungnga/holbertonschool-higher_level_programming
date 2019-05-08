#!/usr/bin/python3

# Write a function that removes all characters c and C from a string


def no_c(my_string):
    new_str = ''
    if my_string:
        for i in my_string:
            if i != 'C' and i != 'c':
                new_str += i
        return new_str
