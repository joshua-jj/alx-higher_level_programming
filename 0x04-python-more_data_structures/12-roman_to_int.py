#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}
    if roman_string and type(roman_string) == str:
        roman_string_list = list(roman_string.upper())
        roman_string_list.reverse()
        length = len(roman_string_list)
        sum = dict[roman_string_list[0]]
        for i in range(1, length):
            if dict[roman_string_list[i]] >= dict[roman_string_list[i-1]]:
                sum += dict[roman_string_list[i]]
            else:
                sum -= dict[roman_string_list[i]]
        return sum
    return 0
