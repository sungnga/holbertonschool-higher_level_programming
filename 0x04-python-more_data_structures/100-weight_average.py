#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        numer = 0
        denom = 0
        for x in my_list:
            numer += x[0] * x[1]
            denom += x[1]
        return numer/denom
    return 0
