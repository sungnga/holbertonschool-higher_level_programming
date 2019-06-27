#!/usr/bin/python3


def islower(c):
    if ord(c) in range(97, 123):
        return True
    else:
        return False


def uppercase(str):
    str1 = ''
    for c in str:
        if islower(c):
            str1 = str1 + chr(ord(c) - 32)
        else:
            str1 = str1 + c
    print("{}".format(str1))
