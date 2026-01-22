#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    i = 0
    while i < len(my_list):
        if my_list[i] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
        i = i + 1
    return new_list
