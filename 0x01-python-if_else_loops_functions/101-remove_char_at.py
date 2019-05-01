#!/usr/bin/python3
def remove_char_at(str, n):
    begin = str[:n]
    end = str[n + 1:]
    return begin + end
