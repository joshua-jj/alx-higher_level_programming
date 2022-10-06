#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    roman_string_list = list(roman_string.upper())
    roman_string_list.reverse()
    length = len(roman_string_list)
    sum = numerals[roman_string_list[0]]
    if type(roman_string) == str or roman_string == None:
        for i in range(1, length):
            if numerals[roman_string_list[i]] >= numerals[roman_string_list[i-1]]:
                sum += numerals[roman_string_list[i]]
            else:
                sum -= numerals[roman_string_list[i]]
        return sum
    return 0
