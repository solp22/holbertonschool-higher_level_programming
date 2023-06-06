#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    max_value = 0
    new_key = ""
    for key in a_dictionary:
        if a_dictionary[key] > max_value:
            max_value = a_dictionary[key]
            new_key = key
    return new_key
