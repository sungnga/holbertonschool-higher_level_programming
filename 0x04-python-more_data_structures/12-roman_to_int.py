#!/usr/bin/python3
def roman_to_int(roman_string):
    a_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string:
        {key: int(value) for key, value in roman_string.iteritems()}
        return a_dict
    return 0
