#!/usr/bin/python3
def roman_to_int(roman_string):
    a_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    if roman_string and type(roman_string) is str:
        for c in range(len(roman_string)):
            if c + 1 >= len(roman_string):
                sum += a_dict[roman_string[c]]
                break
            if a_dict[roman_string[c + 1]] <= a_dict[roman_string[c]]:
                sum += a_dict[roman_string[c]]
            else:
                sum -= a_dict[roman_string[c]]
        return sum
    else:
        return 0
