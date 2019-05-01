#!/usr/bin/python3
import dis
dis.dis(magic_calculation)


def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    return a + b + c
