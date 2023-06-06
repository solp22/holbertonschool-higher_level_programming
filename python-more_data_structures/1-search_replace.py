#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = my_list.copy()
    for i in result:
        if i == search:
            result[i] = replace
    return result