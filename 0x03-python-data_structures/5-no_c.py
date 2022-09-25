#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    for el in str_list:
        if el == 'c' or el == 'C':
            str_list.remove(el)
    return ''.join(str_list)
