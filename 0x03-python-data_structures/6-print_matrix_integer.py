#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for el_list in matrix:
        for el in el_list:
            print('{:d}'.format(el), end =' ')
        print('\n')
