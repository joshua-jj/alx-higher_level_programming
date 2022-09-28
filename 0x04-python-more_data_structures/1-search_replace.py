#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for elm in my_list:
        new_list.append(replace) if elm == search else new_list.append(elm)
    return new_list
