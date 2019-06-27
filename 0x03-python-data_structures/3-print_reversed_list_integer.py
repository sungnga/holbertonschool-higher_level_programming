#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in my_list[::-1]:
            print("{:d}".format(i))

# alternative solution
#    if my_list:
#        my_list.reverse()
#        for i in my_list:
#            print("{:d}".format(i))
