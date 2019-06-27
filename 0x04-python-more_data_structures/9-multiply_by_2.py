#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {key: value*2 for (key, value) in a_dictionary.items()}

''' alternative solution
    b_dictionary = a_dictionary.copy()
    for x in b_dictionary:
        b_dictionary[x] *= 2
    return b_dictionary '''
